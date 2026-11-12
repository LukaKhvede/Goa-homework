function checkAge(age) {
    if (age >= 18) {
        return "You're an adult";
    } else {
        return "You are not an adult";
    }
}

console.log(checkAge(20));
console.log(checkAge(15));
//3
function countLetters(text) {
    return text.length;
}

console.log(countLetters("Hello"));
//4
function sumArray(numbers) {
    let sum = 0;

    for (let i = 0; i < numbers.length; i++) {
        sum += numbers[i];
    }

    return sum;
}

console.log(sumArray([1, 2, 3, 4, 5]));

//5
function square(number) {
    return number * number;
}

console.log(square(5));

//6
function calculate(a = 2, b = 3, c = 4) {
    return (a ** b) * c;
}

console.log(calculate(2, 3, 4));
console.log(calculate(5));
console.log(calculate());

//7

//console.log() უბრალოდ ბეჭდავს ინფორმაციას კონსოლში.
//return აბრუნებს მნიშვნელობას ფუნქციიდან, რათა შემდგომ გამოვიყენოთ.
//return || console.log()
//აბრუნებს მნიშვნელობას	|| ბეჭდავს კონსოლში
//შეგვიძლია შევინახოთ ცვლადში || პირდაპირ ვერ შევინახავთ დაბეჭდილ შედეგს
//ფუნქციის შესრულებას ასრულებს ||  ფუნქციის შესრულებას არ ასრულებს