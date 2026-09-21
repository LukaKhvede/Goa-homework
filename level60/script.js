// 1
let fruits = ["ვაშლი", "ბანანი", "ატამი", "ფორთოხალი"];

console.log("მასივში არის " + fruits.length + " ელემენტი");

//2

let todoList = [];

todoList.push("learn");
todoList.push("workout");
todoList.push("rest");

console.log(todoList);

//3

let numbers = [10, 20, 30, 40, 50];

let removedNumber = numbers.pop();

console.log(removedNumber);

//4

let colors = ["წითელი", "მწვანე", "ლურჯი", "ყვითელი", "იასამნისფერი"];

console.log(colors.at(0));
console.log(colors.at(-1));

//5

let queue = ["გიორგი", "ანა", "ნიკა", "მარიამი"];

queue.shift();

console.log(queue);

//6

let frontEnd = ["HTML", "CSS", "JS"];
let backEnd = ["Node.js", "Python"];

let fullStack = frontEnd.concat(backEnd);

console.log(fullStack);


["HTML", "CSS", "JS", "Node.js", "Python"]

//7

let animals = ["Dog", "Cat", "Bear", "Wolf"];

console.log(animals.indexOf("Cat"));
console.log(animals.indexOf("lion"));

//8

let days = ["ორშაბათი", "სამშაბათი", "ოთხშაბათი", "ხუთშაბათი", "პარასკევი", "შაბათი", "კვირა"];

let workDays = days.slice(0, 5);

console.log(workDays);

//9

let randomMovies = ["Inception", "Interstellar"];

randomMovies.unshift("The Dark Knight");

console.log(randomMovies);

//10

let scores = [50, 65, 78, 92, 45, 88, 99];

let lastThree = scores.slice(-3);

console.log(lastThree);

//11

let searchHistory = [];

searchHistory.push("google.com");
searchHistory.push("github.com");
searchHistory.push("youtube.com");

searchHistory.pop();

searchHistory.push("stackoverflow.com");

console.log(searchHistory.length);
console.log(searchHistory.at(-1));

//12

let shoppingList = ["bread", "milk", "cheese", "eg"];

console.log(shoppingList.indexOf("cheese"));

