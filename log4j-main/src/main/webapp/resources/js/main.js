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
                        title: '<strong style="color: red">WARNING </strong>',
                        icon: 'warning',
                        html:
                        '<p>Scanned website has found CVE-2021-44228!!!</p> ' +
                        '<p>Please check out latest Log4j to update version </p>' +
                        '<p><a href="https://logging.apache.org/log4j/2.x/download.html" target="_blank">https://logging.apache.org/log4j/2.x/download.html</a> </p>'
                        // title: '',
                        // text: 'Scanned website has found CVE-2021-44228, Please check out latest log4j to update your version!',
                        })
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


// When the user clicks the button, open the modal
function aboutMe() {
    var modal = document.getElementById("myModal");
    var span = document.getElementsByClassName("close")[0];
    modal.style.display = "block";
}

// When the user clicks on <span> (x), close the modal
var span = document.getElementsByClassName("close")[0];
span.onclick = function() {
    console.log("CLOSE")
    var modal = document.getElementById("myModal");
    modal.style.display = "none";
}

// When the user clicks anywhere outside of the modal, close it
window.onclick = function(event) {
    var modal = document.getElementById("myModal");
    if (event.target == modal) {
        modal.style.display = "none";
    }
}
// function aboutMe(){
//     Swal.fire({
//         title: '<strong>About ScanJ</strong>',
//         icon: 'info',
//         html:
//             'This website is created for the purpose of helping ' +
//             'businesses, companies, and individuals to carefully check their website ' +
//             'had log4shell vulnerability or not',
//         showCloseButton: true,
//         confirmButtonText:
//             '<i class="fa fa-thumbs-up"></i> Great!',
//         confirmButtonAriaLabel: 'Thumbs up, great!',
//         cancelButtonText:
//             '<i class="fa fa-thumbs-down"></i>',
//         cancelButtonAriaLabel: 'Thumbs down',
//         showClass: {
//             popup: 'animate__animated animate__fadeInDown'
//         },
//         hideClass: {
//             popup: 'animate__animated animate__fadeOutUp'
//         }
//     })
// }

