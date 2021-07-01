function validation() {
    var number = document.getElementById("Number").value;
    var error_message1 = document.getElementById("error_message1");
    var text;

    error_message1.style.padding = "5px";
    error_message1.style =  "margin-bottom: 20px;padding: 0px;color: red;font-weight: 800;text-align: center;font-size: 14px;transition: all 0.5s ease;"

    if (number.length > 10) {
        text = "Please enter valid Mobile Number!";
        error_message1.innerHTML = text;
        return false;
    } else {
        $(this).removeClass("error_message1");
    }
    return true;
}


