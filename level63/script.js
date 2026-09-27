// for (დაწყება; stopping condition; შეცვლა) {
    // კოდი
//}

//magalitad
for (let i = 0; i < 5; i++) {
    console.log(i);
}

//2

for (let i = 25; i <= 30; i++) {
    console.log(i);
}

//3

for (let i = 90; i <= 102; i += 2) {
    console.log(i);
}

//4

for (let i = 90; i >= 50; i--) {
    console.log(i);
}

//5

for (let i = 45; i >= 20; i -= 5) {
    console.log(i);
}

//6

let name = "Luka";

for (let i = 0; i < name.length; i++) {
    console.log(name[i], i);
}

//7

// let name = "Luka";

// for (let i = 0; i < name.length; i++) {
//     console.log(name[i]);
// }

// name.length არის 4, რადგან "Luka"-ში 4 სიმბოლოა.

// ამიტომ:

// i < name.length

// ნიშნავს:

// გაიმეორე loop მანამ, სანამ i სტრინგის სიგრძეზე ნაკლებია.

// ეს ძალიან მოსახერხებელია, რადგან თუ სახელს შევცვლით:

// let name = "Giorgi";

// კოდში არაფრის შეცვლა აღარ გვჭირდება — name.length ავტომატურად გახდება 6.


//8

let numbers = [10, 20, 30, 40, 50];

for (let i = 0; i < numbers.length; i++) {
    console.log(`Number: ${numbers[i]}`);
}