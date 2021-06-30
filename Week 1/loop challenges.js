console.log("Print odds 1-20");
for(var i = 1; i < 20; i++ ) {
    if(i % 2 != 0) {
        console.log(i);
    }
}
console.log();
console.log("Decreases Multiples of 3");
for(var j = 100; j >= 0; j--) {
    if(j % 3 == 0) {
        console.log(j);
    }
}
console.log();
console.log("Print the sequence");
var num = 4;
while(num >= -3.5) {
    console.log(num);
    num -=1.5;
}
console.log();
console.log("Sigma");
var sum = 0;
var iter = 1;
while(iter <= 100) {
    sum += iter;
    iter++;
}
console.log(sum);
console.log();
console.log("Sigma");
var product = 1;
for(var k = 1; k <=12; k++) {
    product *= k;
}
console.log(product);
