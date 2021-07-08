function removeJoin(element) {
    element.remove();
}

var num = [68, 212, 33];
var adding = document.querySelector("#add");
var adding1 = document.querySelector("#add1");
var adding2 = document.querySelector("#add2");

function like() {
    num[0]++;
    adding.innerText = num[0];
}
function like1() {
    num[1]++;
    adding1.innerText = num[1];
}
function like2() {
    num[2]++;
    adding2.innerText = num[2];
}

function displaySearch() {
    var searchReq = document.querySelector("#bar");
    alert(searchReq.value);
}