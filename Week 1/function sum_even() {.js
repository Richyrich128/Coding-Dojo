function sum_even() {
    var sums = 0
    for(var i = 2; i <= 1000; i+2){
        sums += i

    }
    return sums
}
print(sum_even())