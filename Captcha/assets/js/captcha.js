document.addEventListener('DOMContentLoaded', loadCaptcha);

function loadCaptcha() {
	document.getElementById('captcha').innerHTML = '<object style="width: -webkit-fill-available; height: -webkit-fill-available;" id="captcha" data="http://127.0.0.1:8000/captcha/generate" />';
}

function submitCaptcha(){
    var uuid = document.getElementById("uuid").value;
    var uinput = document.getElementById("userinput").value;
    if(!uuid){
        alert("Something is wrong");
        return;
    }

    if(!uinput){
        alert("Captcha is Required");
        return;
    }

    const data = {
        'uid': uuid,
        'ans': uinput
    };

    $.ajax({
        method: "POST",
        url: "http://127.0.0.1:8000/captcha/verify",
        data: JSON.stringify(data),
        contentType: "application/json; charset=utf-8",
        success: function(resp){
            if(resp && resp.success){
                document.getElementById("captcha-form").innerHTML = "<p>Verified</p>";
            }
            else {
                alert('Invalid Captcha');
            }
        },
        fail: function(resp){
            alert('Something is wrong');
        }
    });
}

