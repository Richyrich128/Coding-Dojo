for(var i = 1; i <= 100; i++) {
    var fizz = (i % 3 == 0);
    var buzz = (i % 5 == 0);
    if(fizz && buzz) {
        console.log("FizzBuzz");
    } else if(fizz) {
        console.log("Fizz");
    } else if(buzz) {
        console.log("Buzz");
    } else {
        console.log(i);
    }

}