var count = document.querySelector("#count");
var count1 = document.querySelector("#count1");
var count2 = document.querySelector("#count2");
var amount = [9, 12, 9];
function neilLikes() {
    amount[0]++;
    count.innerText = amount[0] + " like(s)";
}
function nicoleLikes() {
    amount[1]++;
    count1.innerText = amount[1] + " like(s)";
}
function jimLikes() {
    amount[2]++;
    count2.innerText = amount[2] + " like(s)";
}