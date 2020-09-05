var URL

temp_top ="<div class='card'>"
temp_img_front = "<img id='image_place-tag' src="
var img_src
temp_img_back = " width='80%' height='30%'/>"
temp_place_front = "<p id='place-tag'>"
var place_tag
temp_price_front = "<p id='price-tag'>"
var price_tag
temp_explain_front = "<p id='explain-tag'>"
var explain_tag
temp_back = "</p>"
temp_bottom = "</div>"

function getAPI(){
    apiURL =  'http://localhost:8000/' + URL
    var request = new XMLHttpRequest();
    request.open('GET', apiURL, true);
    request.responseType = 'json';

    request.onload = function () {
        var data = this.response
        document.getElementById("apidata").innerText = JSON.stringify(data);
    }

    request.send();
}

function getCards(){
    apiURL =  'http://localhost:8000/api/cards/'
    var request = new XMLHttpRequest();
    request.open('GET', apiURL, true);
    request.responseType = 'json';

    request.onload = function () {
        var data = this.response
        console.log(data.length)
        for(var i=0; i<data.length; i++){
            console.log(data)
            document.getElementById("cards-area").innerHTML += temp_top
                                                            + temp_img_front
                                                            + data[i].photo
                                                            + temp_img_back
                                                            + temp_place_front
                                                            + '場所：' + data[i].place.name + '<br>特徴：' + data[i].chara
                                                            + temp_back
                                                            + temp_price_front
                                                            + '値段：' + data[i].price + '<br>所要時間：' + data[i].duration 
                                                            + temp_back
                                                            + temp_explain_front
                                                            + data[i].explain
                                                            + temp_back
                                                            + temp_bottom
        }
        //    document.getElementById("image_place-tag").src = data[0]["photo"]
        var content = document.getElementById("cards-area").innerHTML
        console.log(content)
    }

    request.send();
}

function setURL(){
    URL = document.getElementById("set_url_text").value;
    document.getElementById("url_text").innerText = URL
}