<html>
  <head>
    <meta http-equiv="Content-Type" content="text/html; charset=UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1" />
    <meta http-equiv="X-UA-Compatible" content="IE=edge" />
    <link href="https://fonts.googleapis.com/css?family=Poppins" rel="stylesheet" />
    <link href="${pageContext.request.contextPath}/resources/css/main.css" rel="stylesheet" />
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
            <li><a href="#">Bao 1</a></li>
            <li><a href="#">Bao 2</a></li>
          </ul></li>
        <li class="drop"><a href="#">Latest Log4J</a>
        <ul class="dropdown">
          <li><a href="#">Log4J Core</a></li>
          <li><a href="#">Log4J Api</a></li>
        </ul>
      </li>
        <li><a href="#">About SCANJ</a></li>
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
  <span class="loader"></span>
    <script src="${pageContext.request.contextPath}/resources/js/extention/choices.js"></script>
  <script src="${pageContext.request.contextPath}/resources/js/main.js"></script>
  </body><!-- This templates was made by Colorlib (https://colorlib.com) -->
</html>
