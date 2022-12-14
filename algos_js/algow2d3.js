/* 
  Given a string containing space separated words
  Reverse each word in the string.
  If you need to, use .split to start, then try to do it without.
*/

const str1 = "hello";
const expected1 = "olleh";

const str2 = "hello world";
const expected2 = "olleh dlrow";

const str3 = "abc def ghi";
const expected3 = "cba fed ihg";

/**
 * Reverses the letters in each words in the given space separated
 * string of words. Does NOT reverse the order of the words themselves.
 * - Time: O(?).
 * - Space: O(?).
 * @param {string} str Contains space separated words.
 * @returns {string} The given string with each word's letters reversed.
 */
function reverseWords(str) {

var newArr = str.split(' ')
var result = []

for(var i = 0; i<newArr.length; i++){
    newStr = newArr[i].split().reverse().join()
    return newStr
}
}
console.log(reverseWords(str1))
// *************************************************

/* 
  Reverse Word Order
  Given a string of words (with spaces)
  return a new string with words in reverse sequence.
*/

const two_str1 = "This is a test";
const two_expected1 = "test a is This";

const two_str2 = "hello";
const two_expected2 = "hello";

const two_str3 = "   This  is a   test  ";
const two_expected3 = "test a is This";

/**
 * Reverses the order of the words but not the words themselves form the given
 * string of space separated words.
 * - Time: O(?).
 * - Space: O(?).
 * @param {string} wordsStr A string containing space separated words.
 * @returns {string} The given string with the word order reversed but the words
 *    themselves are not reversed.
 */
// function reverseWordOrder(str) {
//     var newStr = ''
//     var str = str.split(' ')
//     for(var i = str.length; i>=0; i--){
//         console.log(str[i])
//     }


// }


function reverseWordOrder(wordsStr) {
    // if all spaces
    if (wordsStr == false) {
      return wordsStr;
    }
  
    let currWord = "";
    let reversedWordOrder = "";
  
    for (let i = 0; i < wordsStr.length; i++) {
      const char = wordsStr[i];

    //   variable used to make choices
      const isSpace = char === " ";
      const isLastIteration = i === wordsStr.length - 1;
      const isFirstWord = reversedWordOrder.length === 0;
  
      if (isSpace === false) {
        currWord += char;
      }
  
      if (currWord.length > 0 && (isSpace || isLastIteration)) {
        if (isFirstWord === false) {
          // Add a space to separate words with no extra space at start / end.
          reversedWordOrder = " " + reversedWordOrder;
        }
        // Prepend the word so the order is reversed.
        reversedWordOrder = currWord + reversedWordOrder;
        currWord = "";
      }
    }
    return reversedWordOrder;
  }


  console.log(reverseWordOrder(two_str1))
