
//1

let userAge = 17;

userAge++;

console.log(userAge);

//2

let firstName = "Luka";
let lastName = "Khvedelidze";

console.log(`გამარჯობა, ჩემი სახელია ${firstName} ${lastName}`);

//3

let currentYear = 2026;
let birthYear = 2009;

let calculatedAge = currentYear - birthYear;

console.log(calculatedAge);

//4

let text = "     learning javascript         ";

text = text.trim();
text = text.toUpperCase();

console.log(text);

//5

let score = 50;

score += 25;
score *= 2;
score -= 10;

console.log(score);

//6

let itemPrice = 19.99;

console.log(`itemPrice-ის ტიპია: ${typeof itemPrice}`);

//7

let randomNumber = Math.floor(Math.random() * 10) + 1;

console.log(randomNumber);

//8

let city;

let emptyValue = null;

console.log(city);
console.log(emptyValue);

console.log(typeof city);
console.log(typeof emptyValue);

//9

const favoriteColor = "blue";

console.log(favoriteColor.length);

//10

let pi = 3.14159;

console.log(Math.round(pi));
console.log(Math.floor(pi));

//11

let testNumber = 42.5;

console.log(Number.isInteger(testNumber));