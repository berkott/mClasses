"use strict";

// Data types pretty similar to python, booleans just start with lower case
let michalesAge = 10;
let x = null; // Empty variable basically

// Create a constant
const WEBSITE_URL = "https://google.com";

// double quotes, single quotes <-- basically same thing
// backticks `` <-- similar to f stings in python basically with extended functionality
let streetName = "This is where " + michalesAge + " lives"; // here you could also just use single
let sentence = `This is where ${michalesAge} lives`;

console.log(michalesAge);
console.log(streetName);
console.log(sentence);
console.log(typeof michalesAge);

// --To convert between data types--
// Number()
// String()
// Boolean()

x = 5;
let y = 8;
let z = x ** y; // <-- ** is exponential
// % modulus basically the remainder

z++;
z+=1;
z/=4;
console.log(z);

// In javascript, or is ||, and is &&, not is !
// and is evaluated before or

// Below prints true with == but false with strict equality ===
//     basically datatype and value need to be same
if (0 === false) {
    console.log("3")
} else if ("pie" === `pie`) {
    console.log("2")
} else {
    console.log("1")
}

// A ?? B Nullish coalescing operator --> if A is defined then A, if it isn't then B
console.log(undefined ?? 3);

let username = "Michael";

console.log(`Welcome ${username ?? "Default"}`);

// while loops basically the same
let i = 0;

while (i < 10) {
    console.log(`Joe is ${i}x cooler than you!`);
    i++;
}

for (let i = 0; i < 10; i++) {
    console.log(`Michelle is ${i}x healthier than you!`);
}
// for i in range(10): same as above

// This switch statement below is the same thing as multiple if else statements
// often used for keyboard inputs
let keypressed = 'A';

switch (keypressed) {
    case 'A':
        console.log(1);
        break;
    case 'B':
        console.log(2);
        break;
    default:
        console.log(5);
        break;
}

let myArray = [3, "joe", 'pie'];

// len(myArray) in python = myArray.length in js
for (let i = 0; i < myArray.length; i++) {
    console.log(myArray[i]);
}

niceFunction(4);

function niceFunction(apple) {
    console.log(apple)
}

function whenClicked() {
    console.log(michalesAge);
    console.log(streetName);
    console.log(sentence);
    document.getElementById("my-heading").innerText = "hello";

    // console.log("Michael says hi!");
    // console.log(document.getElementById("Input").value);
}

// https://trinket.io/features/pygame
