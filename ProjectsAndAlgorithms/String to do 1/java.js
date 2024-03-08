// 2.Create a JavaScript function that given a string, returns the integer made from the string’s digits. You are allowed to use isNaN() and Number().

function getDigits(str) {
    let result = '';
    for (let char of str) {
        if (!isNaN(parseInt(char))) {
            result += char;
        }
    }
    return parseInt(result);
}

// Examples
console.log(getDigits("abc8c0d1ngd0j0!8"));  // Output: 801008
console.log(getDigits("0s1a3y5w7h9a2t4?6!8?0")); // Output: 1357924680

// 3.Create a function that, given a string, returns the string’s acronym (first letter of the word capitalized). You are allowed to use .split() and .toUpperCase().

function acronym(str) {
    let words = str.split(' ');
    let result = '';
    for (let word of words) {
        if (word !== '') {
            result += word[0].toUpperCase();
        }
    }
    return result;
}

// Examples
console.log(acronym(" there's no free lunch - gotta pay yer way. ")); // Output: "TNFL-GPYW"
console.log(acronym("Live from New York, it's Saturday Night!"));    // Output: "LFNYISN"

//4.Create a function that, given a string, returns the number of non-space characters found in the string. 

function countNonSpaces(str) {
    let count = 0;
    for (let char of str) {
        if (char !== ' ') {
            count++;
        }
    }
    return count;
}

// Examples
console.log(countNonSpaces("Honey pie, you are driving me crazy")); // Output: 29
console.log(countNonSpaces("Hello world !")); // Output: 11

//5.Create a function that, given an array of strings and a numerical value, returns an array that only contains strings longer than or equal to the given value.

function removeShorterStrings(arr, length) {
    return arr.filter(str => str.length >= length);
}

// Examples
console.log(removeShorterStrings(['Good morning', 'sunshine', 'the', 'Earth', 'says', 'hello'], 4)); // Output: ['Good morning', 'sunshine', 'Earth', 'says', 'hello']
console.log(removeShorterStrings(['There', 'is', 'a', 'bug', 'in', 'the', 'system'], 3)); // Output: ['There', 'bug', 'the', 'system']
