$(document).ready(function(){
$.ajaxSetup({
        beforeSend: function (xhr, settings) {
            function getCookie(name) {
                var cookieValue = null;
                if (document.cookie && document.cookie != '') {
                    var cookies = document.cookie.split(';');
                    for (var i = 0; i < cookies.length; i++) {
                        var cookie = jQuery.trim(cookies[i]);
                        // Does this cookie string begin with the name we want?
                        if (cookie.substring(0, name.length + 1) == (name + '=')) {
                            cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                            break;
                        }
                    }
                }
                return cookieValue;
            }

            if (!(/^http:.*/.test(settings.url) || /^https:.*/.test(settings.url))) {
                // Only send the token to relative URLs i.e. locally.
                xhr.setRequestHeader("X-CSRFToken", getCookie('csrftoken'));
            }
        }
    });


  function getdata(){
  s = $('#employee').val();
  b = $('#batchid').val();
            var data = new FormData();
            data.append("username", s)
            data.append("batch", b)
                    $.ajax({
                            type: 'POST',
                            contentType: "application/json; charset=utf-8",
                            contentType: false,
                            processData: false,
                            url: '/Payroll/getdata/',
                            data: data,
                            async: false,
                            success: function (response) {
                                if(response.status == "valid"){
                                $('#totalhours').html(response.hours);
                                $('#deductions').html(response.totaldeductions);
                                $('#earnings').html(response.earnings);
                                $('#tearnings').html(response.total_earnings);
                                $('#salary').html(response.data.base_salary);
                                $('#ha').html(response.data.Housing_Allowance);
                                $('#ta').html(response.data.Transport_Allowance);
                                $('#ot').html(response.data.otherallowance);
                                $('#gosi').html(response.tax);
                                $('#tearnings_hidden').val(response.total_earnings)
                                }
                                else{
                                     alert('No Data Found')
                                }
                            },
                            error: function () {
                                alert('error')
                            }
                        });
  }
getdata();
  $(document).on("change","#employee",function () {
            getdata();

            });

$(document).on("input","#addition",function () {
            $('#tearnings').html(parseInt($('#tearnings_hidden').val())+parseInt($(this).val()));

            });
})
