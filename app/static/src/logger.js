const ul = document.getElementById('ulBody');

var interval = setInterval(check_logs, 500);

var live_button = document.getElementById("live_button");

live_button.is_live = true;
live_button.interval = interval;

live_button.addEventListener("click", change_live_status);

function change_live_status(event) {
    if (live_button.is_live){
        live_button.is_live = false;

        live_button.classList.remove("btn-success");
        live_button.classList.add("btn-danger");

        clearInterval(live_button.interval);
        // window.clearInterval(intervalID)
    }
    else {
        live_button.is_live = true;

        live_button.classList.remove("btn-danger");
        live_button.classList.add("btn-success");

        live_button.interval = setInterval(check_logs, 500);
    }
}

function check_logs(event) {
    let xhr = new XMLHttpRequest();

    xhr.onreadystatechange = function() {
        if (xhr.readyState == XMLHttpRequest.DONE && xhr.status == 200) {
            // console.log(xhr.responseText);
            ul.innerHTML = xhr.responseText;
            jQuery('ul').animate({scrollTop: ul.scrollHeight}, "slow");
            // jQuery('ul').animate({scrollTop: ul.scrollHeight+50}, "slow");
            // ul.scrollBy (ul.scrollHeight);
            // $(document).ready(function(){
            //     $('body').scrollTop($('ul li').last().position().top + $('ul li').last().height());
            // });
            // const connection = new http.Connection('http://69.69.69.73:5050');
            // connection.addHeader('authorization', `JWT ${JSON.parse(xhr.responseText)['access_token']}`);

            // myHeaders = new Headers();

            // console.log(myHeaders);
            // myHeaders.append('authorization', `JWT ${JSON.parse(xhr.responseText)['access_token']}`);
            // console.log(myHeaders.get('authorization'));

            // const supabase = createClient("https://xyzcompany.supabase.co", "public-anon-key")
            // const { user, error } = supabase.auth.setAuth(`JWT ${JSON.parse(xhr.responseText)['access_token']}`)
            // window.location = '/realtime_info';

            // console.log(xhr.responseText);
        }
    }

    xhr.open('GET', '/logger/get_logs', true);

    // console.log("Sending");

    // var formData = new FormData(form);

    // xhr.setRequestHeader('Content-Type', 'application/json;charset=UTF-8');
    xhr.send();
    
    // console.log(xhr.response);
    
    // event.preventDefault();
}

// form.addEventListener('submit', logSubmit);