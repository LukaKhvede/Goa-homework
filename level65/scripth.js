let i = 1;

while (i <= 10) {
    console.log(i);
    i++;
}
//3
let m = 1;
let sum = 0;

while (m <= 100) {
    sum += m;
    m++;
}

console.log(sum);

//4

// let number = 5;
// let i = 1;

// while (i <= 10) {
//     console.log(number * i);
//     i++;
// }

//5

// let numbers = [1, 4, 7, 10, 12, 15, 18];
// let i = 0;

// while (i < numbers.length) {
//     if (numbers[i] % 2 === 0) {
//         console.log(numbers[i]);
//     }
//     i++;
// }

//6

// let password = "12345";
// let userPassword = "";

// while (userPassword !== password) {
//     userPassword = prompt("შეიყვანე პაროლი:");
// }

// console.log("სწორი პაროლია!");

//7

// let numbers = [2, 4, 6, 8, 10];
// let i = 0;

// while (i < numbers.length) {
//     console.log(numbers[i] * 2);
//     i++;
// }

//8

// let numbers = [5, 8, 10, 14, 20];
// let i = 0;

// while (i < numbers.length) {
//     console.log(numbers[i] % 3);
//     i++;
// }

//9

for (let i = 0; i < 5; i++) {
    let row = "";

    for (let j = 0; j < 5; j++) {
        row += "* ";
    }

    console.log(row);
}

//10

// for (let i = 1; i <= 10; i++) {

//     for (let j = 1; j <= 10; j++) {
//         console.log(i * j);
//     }

// }

//11

// let array1 = [1, 2, 3, 4, 5];
// let array2 = [3, 5, 7, 9, 1];

// for (let i = 0; i < array1.length; i++) {

//     for (let j = 0; j < array2.length; j++) {

//         if (array1[i] === array2[j]) {
//             console.log(array1[i]);
//         }

//     }

// }

//12

// let matrix = [
//     [1, 2, 3],
//     [4, 5, 6],
//     [7, 8, 9]
// ];

// let sum = 0;

// for (let i = 0; i < matrix.length; i++) {

//     for (let j = 0; j < matrix[i].length; j++) {
//         sum += matrix[i][j];
//     }

// }

// console.log(sum);