<html>
  <head>
    <meta http-equiv="Content-Type" content="text/html; charset=UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1" />
    <meta http-equiv="X-UA-Compatible" content="IE=edge" />
    <link href="https://fonts.googleapis.com/css?family=Poppins" rel="stylesheet" />
    <link href="${pageContext.request.contextPath}/resources/css/main.css" rel="stylesheet" />
    <link
            rel="stylesheet"
            href="https://cdnjs.cloudflare.com/ajax/libs/animate.css/4.1.1/animate.min.css"
    />
    <script src="https://cdn.jsdelivr.net/npm/sweetalert2@10"></script>
    <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.5.1/jquery.min.js"></script>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.12.9/umd/popper.min.js" integrity="sha384-ApNbgh9B+Y1QKtv3Rn7W3mgPxhU9K/ScQsAP7hUibX39j7fakFPskvXusvfa0b4Q" crossorigin="anonymous"></script>
  </head>
  <div>
  <div class="logo">
    <img src="${pageContext.request.contextPath}/resources/images/u3.png">
    <nav class="nav">
      <ul>
        <li class="drop2"><a href="#">About CVE-2021-44228</a>
          <ul class="dropdown2">
            <li><a target="_blank" href="https://logging.apache.org/log4j/2.x/">Apache Log4J 2</a></li>
            <li><a target="_blank" href="https://blog.cloudflare.com/inside-the-log4j2-vulnerability-cve-2021-44228/">Inside the Log4j2 vulnerability</a></li>
            <li><a target="_blank" href="https://www.fastly.com/blog/digging-deeper-into-log4shell-0day-rce-exploit-found-in-log4j">Digging deeper into Log4Shell</a></li>
            <li><a target="_blank" href="https://raxis.com/blog/log4j-exploit">How to Exploit and Test this Critical Vulnerability</a></li>
          </ul></li>
        <li class="drop"><a href="#">Latest Log4J</a>
          <ul class="dropdown">
            <li style="min-width: 150px;"><a target="_blank" href="https://www.bleepingcomputer.com/news/security/dutch-cybersecurity-agency-warns-of-lingering-log4j-risks/">Warns of lingering Log4j risks</a></li>
            <li style="min-width: 150px;"><a target="_blank" href="https://www.bleepingcomputer.com/news/security/state-hackers-use-new-powershell-backdoor-in-log4j-attacks/">Log4j Attacks</a></li>
            <li style="min-width: 150px;"><a target="_blank" href="https://mvnrepository.com/artifact/org.apache.logging.log4j/log4j-core/2.17.2">Log4J Core</a></li>
            <li style="min-width: 150px;"><a target="_blank" href="https://mvnrepository.com/artifact/org.apache.logging.log4j/log4j-api/2.17.2">Log4J Api</a></li>
        </ul>
      </li>
        <li><a href="#" onclick="aboutMe()">About SCANJ</a></li>
      </ul>
    </nav>
  </div>
    <div class="s130">
      <form id="formAction" method="POST">
        <div class="inner-form">
          <div class="input-field first-wrap">
            <div class="svg-wrapper">
              <svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24">
                <path d="M15.5 14h-.79l-.28-.27C15.41 12.59 16 11.11 16 9.5 16 5.91 13.09 3 9.5 3S3 5.91 3 9.5 5.91 16 9.5 16c1.61 0 3.09-.59 4.23-1.57l.27.28v.79l5 4.99L20.49 19l-4.99-5zm-6 0C7.01 14 5 11.99 5 9.5S7.01 5 9.5 5 14 7.01 14 9.5 11.99 14 9.5 14z"></path>
              </svg>
            </div>
            <input id="search" name="search" type="text" placeholder="What are you looking for?" />
          </div>
          <div class="input-field second-wrap">
            <button class="btn-search" type="submit">SCAN</button>
          </div>
        </div>
       <!-- <span class="info">ex. Game, Music, Video, Photography</span> -->
      </form>

    </div>

    <div class="footer" style="display: inline;">
      <div class="text" style="float: left; width: 50%; margin-left: 2em">
      <p style="font-size: 72px;font-weight: 700;color: #FFFFFF; margin-bottom: 30px;">Critical Impact</p>
      <p style="font-size: 30px;font-weight: 700;color: #FFFFFF">Apache Log4j Remote Code Execution Vulnerability</p>
      <p style="font-size: 20px;font-weight: 700;color: #FFFF00">CVE-2021-44228</p>
      <p style="font-size: 18px;color: #FFFFFF"">A flaw was found in the Apache Log4j logging library in versions

        from 2.0.0 and before 2.15.0. A remote attacker who can control log messages
        
        or log message parameters, can execute arbitrary code on the server via JNDI LDAP endpoint.</p>
      </div>
<%--      <div class = "left" style="float: right; width: 40%; text-align: center;">--%>
<%--        <img src="/resources/images/u1.png"/>--%>
<%--      </div>--%>
    </div>
    <div id="myModal" class="modal">

      <!-- Modal content -->
      <div class="modal-content">
        <div class="modal-header">
          <span class="close" onclick="close()">&times;</span>
          <p style="font-size: 38px;font-weight: 700;text-align: center;">ABOUT SCANJ</p>
        </div>
        <div class="modal-body">
          <p style="font-size: 22px">Information technology is developing day by day. Thousands of applications are developed based on the Java programming language every day. With the existing vulnerability, it will be an excellent opportunity for hackers to attack and perform malicious actions on the server.
          <p style="font-size: 22px">Deploy cryptocurrency mining software like xmrig/kinsing</p>
          <p style="font-size: 22px"> Ransomware Deployment</p>
          <p style="font-size: 22px"> Install Reverse shells</p>
          <p style="font-size: 22px"> With the desire to solve the above problems, we learned about how attackers find and exploit vulnerabilities and develop an application on the web interface so that users only need to enter the URL on the location. The position to be scanned is that the application can automatically detect vulnerabilities and warn users to have remedial methods before being exploited by hackers</p>
        </div>
      </div>
    </div>
  <span class="loader"></span>
    <script src="${pageContext.request.contextPath}/resources/js/extention/choices.js"></script>
  <script src="${pageContext.request.contextPath}/resources/js/main.js"></script>
  </body><!-- This templates was made by Colorlib (https://colorlib.com) -->
</html>
