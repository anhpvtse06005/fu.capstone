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
                } else if(response == '2'){
                    Swal.fire({
                        icon: 'success',
                        title: '',
                        text: 'Targets do not seem to be vulnerable!',
                    })
                }else if(response == '1'){
                    Swal.fire({
                        icon: 'warning',
                        title: '',
                        text: 'DIEEEEEEEEEEEEEEE!',})
                }
            }, 100);

        },
        error: function (request, status, error) {

        }
    });
});

