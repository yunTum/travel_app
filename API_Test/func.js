
function getAPI(){
    URL =  'http://localhost:8000/api/version/'
    var request = new XMLHttpRequest();
    request.open('GET', URL, true);
    request.responseType = 'json';

    request.onload = function () {
        document.getElementById("apidata").innerText = this.response;
        console.log(this.response);
    }

    request.send();
}