/* 
  Given an arr and a separator string, output a string of every item in the array separated by the separator.
  
  No trailing separator at the end
  Default the separator to a comma with a space after it if no separator is provided
*/

const arr1 = [1, 2, 3];
const separator1 = ", ";
const expected1 = "1, 2, 3";

const arr2 = [1, 2, 3];
const separator2 = "-";
const expected2 = "1-2-3";

const arr3 = [1, 2, 3];
const separator3 = " - ";
const expected3 = "1 - 2 - 3";

const arr4 = [1];
const separator4 = ", ";
const expected4 = "1";

const arr5 = [];
const separator5 = ", ";
const expected5 = "";

function join(arr, separator) {
//your code here
    var result = "";

    if( arr.length > 0) {
        result += arr[0];
    }
    for(let i = 1; i <= arr.length - 1; i++) {
        result += separator + arr[i];  
    }
    return result ;
}

function join1(arr, separator) {
    return arr.join(separator);
}


console.log(join(arr1, separator1))
console.log(join(arr2, separator2))
console.log(join(arr3, separator3))
console.log(join(arr4, separator4))
console.log(join(arr5, separator5))
console.log()
console.log(join1(arr1, separator1))
console.log(join1(arr2, separator2))
console.log(join1(arr3, separator3))
console.log(join1(arr4, separator4))
console.log(join1(arr5, separator5))
