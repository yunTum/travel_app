var URL
function getAPI(){
    apiURL =  'http://localhost:8000/' + URL
    var request = new XMLHttpRequest();
    request.open('GET', apiURL, true);
    request.responseType = 'json';

    request.onload = function () {
        console.log(this.response);
        document.getElementById("apidata").innerText = JSON.stringify(this.response);
    }

    request.send();
}

function setURL(){
    URL = document.getElementById("set_url_text").value;
    document.getElementById("url_text").innerText = URL
}