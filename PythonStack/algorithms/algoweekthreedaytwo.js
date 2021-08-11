/* 
Given in an alumni interview in 2021.
String Encode
You are given a string that may contain sequences of consecutive characters.
Create a function to shorten a string by including the character,
then the number of times it appears. 


If final result is not shorter (such as "bb" => "b2" ),
return the original string.
*/

const str1 = "aaaabbcddd";
const expected1 = "a4b2c1d3";

const str2 = "";
const expected2 = "";

const str3 = "a";
const expected3 = "a";

const str4 = "bbcc";
const expected4 = "bbcc";

/**
 * Encodes the given string such that duplicate characters appear once followed
* by a number representing how many times the char occurs only if the
* character occurs more than two time.
* - Time: O(?).
* - Space: O(?).
* @param {string} str The string to encode.
* @returns {string} The given string encoded.
*/
function encodeStr(str) {
    var result = "";
    if (str != "") {
        var track = str.charAt(0);
        var count = 1;
        for(let i = 1; i < str.length; i++){
            if(str.charAt(i) == track) {
                count++;
            } else {
                result += track + count.toString();
                track = str.charAt(i);
                count = 1;
            }
        }
        if (result.length >= str.length) {
            return str
        } 
    }
    return result
}
console.log(encodeStr("aaaabbcddd"));
console.log(encodeStr(""));
console.log(encodeStr("a"));
console.log(encodeStr("bbcc"));

/* 
String Decode  
*/

const stri1 = "a3b2c1d3";
const expect1 = "aaabbcddd";

const stri2 = "a3b2c12d10";
const expect2 = "aaabbccccccccccccdddddddddd";

/**
 * Decodes the given string by duplicating each character by the following int
* amount if there is an int after the character.
* - Time: O(?).
* - Space: O(?).
* @param {string} str An encoded string with characters that may have an int
*    after indicating how many times the character occurs.
* @returns {string} The given str decoded / expanded.
*/
function decodeStr(str) {
    var result = "";
    if (str != ""){
        for(let i = 0; i < str.length; i +=2 ){
            for(let j = 0; j < Number(str.charAt(i+1)); j++ ) {
                result += str.charAt(i);
            }
        }
    }
    return result;
}

console.log(decodeStr(stri1));
console.log(decodeStr(stri2));
