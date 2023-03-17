// console.log("Hello, world");

// const http = require('@jetbrains/youtrack-scripting-api/http');

const form = document.getElementById('authForm');

function logSubmit(event) {
    // log.textContent = `Form Submitted! Time stamp: ${event.timeStamp}`;
    
    let xhr = new XMLHttpRequest();

    xhr.onreadystatechange = function() {
        if (xhr.readyState == XMLHttpRequest.DONE && xhr.status == 200) {
            const connection = new http.Connection('http://69.69.69.73:5050');
            connection.addHeader('authorization', `JWT ${JSON.parse(xhr.responseText)['access_token']}`);

            // myHeaders = new Headers();

            // console.log(myHeaders);
            // myHeaders.append('authorization', `JWT ${JSON.parse(xhr.responseText)['access_token']}`);
            // console.log(myHeaders.get('authorization'));

            // const supabase = createClient("https://xyzcompany.supabase.co", "public-anon-key")
            // const { user, error } = supabase.auth.setAuth(`JWT ${JSON.parse(xhr.responseText)['access_token']}`)
            window.location = '/realtime_info';

            console.log();
        }
    }

    xhr.open('POST', '/auth', true);

    console.log("Sending");

    var formData = new FormData(form);

    xhr.setRequestHeader('Content-Type', 'application/json;charset=UTF-8');
    xhr.send(JSON.stringify({ "username": formData.get("username"), "password": formData.get("password") }));
    
    console.log(xhr.response);
    
    event.preventDefault();
}
  
form.addEventListener('submit', logSubmit);