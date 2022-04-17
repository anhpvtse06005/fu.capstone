$("#formAction").submit(function (event) {
    event.preventDefault();
    var search = {}
    search["web"] = $("#search").val();
    console.log(search);
    $.ajax({
        url: "/webScan/scan",
        method: "POST",
        data: JSON.stringify(search),
        enctype: 'application/json',
        processData: false,
        contentType: "application/json",
        cache: false,
        dataType: 'json',
        timeout: 600000,
        beforeSend: function () {
        },
        success: function (response) {
            window.setTimeout(function () {
                if(response == '0'){
                    Swal.fire({
                        icon: 'error',
                        title: 'Oops...',
                        text: 'Please enter valid website!',
                        showConfirmButton: false,
                        timer: 1500,

                    })
                } else if(response == '1'){
                    Swal.fire({
                        icon: 'success',
                        title: '',
                        text: 'Targets do not seem to be vulnerable!',
                    })
                }else if(response == '2'){
                    Swal.fire({
                        icon: 'warning',
                        title: '',
                        text: 'Scanned website has found CVE-2011-44228, Please check out latest log4j to update your version!',})
                }
            }, 100);

        },
        error: function (request, status, error) {

        }
    });
});
$(function(){
    $(".drop")
        .mouseover(function() {
            $(".dropdown").show(300);
        });
    $(".drop")
        .mouseleave(function() {
            $(".dropdown").hide(300);
        });
})

$(function(){
    $(".drop2")
        .mouseover(function() {
            $(".dropdown2").show(300);
        });
    $(".drop2")
        .mouseleave(function() {
            $(".dropdown2").hide(300);
        });
})

function aboutMe(){
    Swal.fire({
        title: '<strong>About ScanJ</strong>',
        icon: 'info',
        html:
            'Information technology is developing day by day. Thousands of applications are developed based on the Java programming language every day. With the existing vulnerability, it will be an excellent opportunity for hackers to attack and perform malicious actions on the server. \n' +
            'Deploy cryptocurrency mining software like xmrig/kinsing\n' +
            'Ransomware Deployment\n' +
            'Install Reverse shells\n' +
            'With the desire to solve the above problems, we learned about how attackers find and exploit vulnerabilities and develop an application on the web interface so that users only need to enter the URL on the location. The position to be scanned is that the application can automatically detect vulnerabilities and warn users to have remedial methods before being exploited by hackers',
        showCloseButton: true,
        confirmButtonText:
            '<i class="fa fa-thumbs-up"></i> Great!',
        confirmButtonAriaLabel: 'Thumbs up, great!',
        cancelButtonText:
            '<i class="fa fa-thumbs-down"></i>',
        cancelButtonAriaLabel: 'Thumbs down',
        showClass: {
            popup: 'animate__animated animate__fadeInDown'
        },
        hideClass: {
            popup: 'animate__animated animate__fadeOutUp'
        }
    })
}

