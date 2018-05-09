function addToCart(pk) {
    var currentCart = getCookie('cart');
    if (currentCart === 'None') {
        currentCart = String(pk) + ','
    } else {
        currentCart += String(pk) + ',';
    }

    setCookie('cart', currentCart, 1);
}

function setCookie(cname, cvalue, exdays) {
    var d = new Date();
    d.setTime(d.getTime() + (exdays*24*60*60*1000));
    var expires = "expires="+ d.toUTCString();
    document.cookie = cname + "=" + cvalue + "; " + expires + "; path=/";
}

function getCookie(cname) {
    var name = cname + "=";
    var decodedCookie = decodeURIComponent(document.cookie);
    var ca = decodedCookie.split(';');
    for(var i = 0; i <ca.length; i++) {
        var c = ca[i];
        while (c.charAt(0) == ' ') {
            c = c.substring(1);
        }
        if (c.indexOf(name) == 0) {
            return c.substring(name.length, c.length);
        }
    }
    return "";
}

function getSuggestions() {
    var myCSRF = getCookie('csrftoken');
    console.log('hey');

    var inputValue = document.getElementById("search-field").value;

    var xhttp = new XMLHttpRequest();

    if (inputValue !== undefined && inputValue.length >= 2){
        xhttp.open("POST", "/store/ajax/", true);
        xhttp.setRequestHeader("X-CSRFToken", myCSRF);
        xhttp.onreadystatechange = function(){
            if (xhttp.readyState === 4 && xhttp.status === 200){
                console.log(xhttp.responseText);
                var suggestions_array = JSON.parse(xhttp.responseText);

                createHtmlList(suggestions_array);
            }
        };
        xhttp.send(inputValue);
    } else {
        document.getElementById('suggestions').style.display = "none";
    }
}

// valores de readyState: 0 (petición no inicializada), 1 (petición establecida), 2 (petición enviada),
//                        3 (petición está siendo procesada), 4 (petición finalizada)


function createHtmlList(arr){
    document.getElementById('suggestions').style.display = "block";
    document.getElementById('suggestions').innerHTML = "";
    var i;
    for (i in arr){
        var list_element = document.createElement("li");
        var text_node = document.createTextNode(arr[i]);
        list_element.onclick = function(){
                    document.getElementById('search-field').value = this.childNodes[0].nodeValue;
                };
        list_element.appendChild(text_node);
        document.getElementById('suggestions').appendChild(list_element);
    }
}
