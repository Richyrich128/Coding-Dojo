function reverse(arr) {
    var array = [];
    for(var i = arr.length - 1; i >= 0 ;i--) {
        array[Math.abs(i - (arr.length - 1))] = arr[i];
    }
    return array;
}

console.log(reverse([1,2,3,4,5]));