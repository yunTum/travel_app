var URL
function getAPI(){
    apiURL =  'http://localhost:8000/' + URL
    var request = new XMLHttpRequest();
    request.open('GET', apiURL, true);
    request.responseType = 'json';

    request.onload = function () {
        var data = this.response

        document.getElementById("apidata").innerText = JSON.stringify(data);

        if (data[0]["photo"]){
            document.getElementById("image_place").src = data[0]["photo"]
        }
        else{
            document.getElementById("image_place").src = ""
        }
    }

    request.send();
}

function setURL(){
    URL = document.getElementById("set_url_text").value;
    document.getElementById("url_text").innerText = URL
}