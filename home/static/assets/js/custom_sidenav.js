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



//$(".btnaddBenefit").on('click',function(){
//
//    $('.benifit-card-btn').html($(this).attr('',''))
//
//});

$('.cont-btn').on('click',function(){
    if($('#personal').hasClass('active'))
    {
        fname=$('#firstname').val()
        lname=$('#lastname').val()
        uname=$('#workemail').val()
        password=$('#pass').val()
        lname=$('#lastname').val()
        dob=$('#dob').val()
        if(fname != "" && lname != "" && dob != ""){
            if($('#empid').val() == ""){
             if(uname != "" && password != "" ){
                $('#personal').removeClass('active');
                    $('#job').addClass('active')
                }

             }
             else{
             $('#personal').removeClass('active');
                    $('#job').addClass('active')
             }
        }

    }
    else if($('#job').hasClass('active'))
    {
        if($('#hdate').val() != ""){
        var x = saveemployee();
        if(x == true){
        fname=$('#firstname').val()
        lname=$('#lastname').val()
             $('#empname').html(fname+' '+lname)

                 $('#personal').removeClass('active');
                 $('#job').removeClass('active');
                 $('#contract').addClass('active')
                 }
        }

    }
    else if($('#contract').hasClass('active'))
    {
    sdate = $('#sdate').val();
  endDate = $('#endDate').val();
    bs = $('#bs').val();
  HA = $('#HA').val();
  TA = $('#TA').val();
  OA = $('#OA').val();

  if(bs != "" && HA != "" && TA != "" && OA != "" && sdate != "" && endDate != ""){
         $('#personal').removeClass('active');
         $('#job').removeClass('active');
         $('#contract').removeClass('active');
//         $('#vacation').addClass('active');
         $('#schedule').addClass('active');
         }
    }
    else if($('#vacation').hasClass('active'))
    {
        $('#personal').removeClass('active');
         $('#job').removeClass('active');
         $('#contract').removeClass('active');
         $('#vacation').removeClass('active');
         $('#schedule').addClass('active');
    }
    else if($('#schedule').hasClass('active'))
    {
    shiftstart = $('#shiftstart').val();
  shiftend = $('#shiftend').val();
  workhours = $('#workhours').val();
  if(shiftstart != "" && shiftend != "" && workhours != "" ){
        $('#personal').removeClass('active');
         $('#job').removeClass('active');
         $('#contract').removeClass('active');
         $('#vacation').removeClass('active');
         $('#schedule').removeClass('active');
         $('#benifits').addClass('active');
         }
    }
    else if($('#benifits').hasClass('active'))
    {
      gosi = $('#gosi').val();

    if(gosi != "0" ){
    var x = savecontract();
     if(x == true){
        $('#personal').removeClass('active');
         $('#job').removeClass('active');
         $('#contract').removeClass('active');
         $('#vacation').removeClass('active');
         $('#schedule').removeClass('active');
         $('#benifits').removeClass('active');
         $('#complete').addClass('active');
         }
         }
    }
    else if($('#complete').hasClass('active'))
    {
        location.href="/Employee/viewemployees/"
    }
});


function saveemployee(){
  empid = $('#empid').val();
  firstname = $('#firstname').val();
  lastname = $('#lastname').val();
  workemail = $('#workemail').val();
  pass = $('#pass').val();
  dob = $('#dob').val();
  gender = $('input[name="gender"]:checked').val();
  nationality = $('#nationality').val();
  idtype = $('#idtype').val();
  idnumber = $('#idnumber').val();

  jtitle = $('#jtitle').val();
  EmployeeGrade = $('#EmployeeGrade').val();
  EmployeeLevel = $('#EmployeeLevel').val();
  ccenter = $('#costcenter').val();
  empno = $('#enum').val();
  hdate = $('#hdate').val();
  loc = $('#location').val();
  coach = $('#coach').val();
  dept = $('#department').val();
  manager = $('#manager').val();
  ishr = $('#ishr').val();
  ismanager = $('#ismanager').val();

  var data = new FormData();
  data.append("empid", empid)
  data.append("firstname", firstname)
  data.append("lastname", lastname)
  data.append("username", workemail)
  data.append("password", pass)
  data.append("dob", dob)
  data.append("gender", gender)
  data.append("nationality", nationality)
  data.append("idtype", idtype)
  data.append("idnumber", idnumber)

  data.append("jtitle", jtitle)
  data.append("EmployeeGrade", EmployeeGrade)
  data.append("EmployeeLevel", EmployeeLevel)
  data.append("costcenter", ccenter)
  data.append("enum", empno)
  data.append("hdate", hdate)
  data.append("location", loc)
  data.append("coach", coach)
  data.append("dept", dept)
  data.append("manager", manager)
  data.append("ishr", ishr)
  data.append("ismanager", ismanager)
  var r = false;
      $.ajax({
              type: 'POST',
              contentType: "application/json; charset=utf-8",
              contentType: false,
              processData: false,
              url: '/Employee/saveemployee/',
              data: data,
              async: false,
              success: function (response) {
                  if(response.status == "success"){

                  $('#empid').val(response.id)
                  r=true;
                  }
                  else if(response.status == "exists"){
                                          $('#job').removeClass('active')
                       $('#personal').addClass('active');
                       swal("User Exists","Kindly enter different email address","error")
                  }
                  else{
                  alert('Error')
              }
              },
              error: function () {
                  alert('error')
              }
      });
      return r;
  }

function savecontract(){
  empid = $('#empid').val();
  cid = $('#cid').val();
  emptype = $('#emptype').val();
  contPerid = $('#contPerid').val();
  sdate = $('#sdate').val();
  endDate = $('#endDate').val();
  notPeriod = $('#notPeriod').val();
  probPeriod = $('#probPeriod').val();
  bs = $('#bs').val();
  HA = $('#HA').val();
  TA = $('#TA').val();
  OA = $('#OA').val();

  shiftstart = $('#shiftstart').val();
  shiftend = $('#shiftend').val();
  workhours = $('#workhours').val();
  lunch = $('#break').val();
  gosi = $('#gosi').val();

  var data = new FormData();
  data.append("empid", empid)
  data.append("cid", cid)
  data.append("emptype", emptype)
  data.append("contPerid", contPerid)
  data.append("sdate", sdate)
  data.append("endDate", endDate)
  data.append("notPeriod", notPeriod)
  data.append("probPeriod", probPeriod)
  data.append("bs", bs)
  data.append("HA", HA)
  data.append("TA", TA)
  data.append("OA", OA)

  data.append("shiftstart", shiftstart)
  data.append("shiftend", shiftend)
  data.append("workhours", workhours)
  data.append("lunch", lunch)
  data.append("gosi", gosi)
  var r = false;
      $.ajax({
              type: 'POST',
              contentType: "application/json; charset=utf-8",
              contentType: false,
              processData: false,
              url: '/Employee/savecontract/',
              data: data,
              async: false,
              success: function (response) {
                  if(response.status == "success"){

                  $('#cid').val(response.id)
                  r=true;
                  }
                  else{
                  swal("Error","Something Went Wrong!","error")
              }
              },
              error: function () {
                  swal("Error","Something Went Wrong!","error")
              }
      });
      return r;
  }
  });

  function Employees(evt, cityName) {
  // Declare all variables
  var i, tabcontent, tablinks;

  // Get all elements with class="tabcontent" and hide them
  tabcontent = document.getElementsByClassName("tabcontent");
  for (i = 0; i < tabcontent.length; i++) {
    tabcontent[i].style.display = "none";
  }

  // Get all elements with class="tablinks" and remove the class "active"
  tablinks = document.getElementsByClassName("tablinks");
  for (i = 0; i < tablinks.length; i++) {
    tablinks[i].className = tablinks[i].className.replace(" active", "");
  }

  // Show the current tab, and add an "active" class to the link that opened the tab
  document.getElementById(cityName).style.display = "block";
  evt.currentTarget.className += " active";
}