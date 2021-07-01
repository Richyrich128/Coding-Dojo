var count = document.querySelector("#count");
var amount = 3;
function moreLikes() {
    amount++;
    count.innerText = amount + " like(s)";
}