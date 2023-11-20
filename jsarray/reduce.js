const numbers = [1,-1,2,3];
/*
let sum = 3;
for (let n of numbers)
    sum+= n;
*/
const item = numbers.reduce((accumulator, currentValue) => accumulator += currentValue , 3);

const words = ["paperino","pluto","gargamella","suca",4]

const item2 = words.reduce((accumulator, currentValue) => accumulator += currentValue + "\t" , "Le parole: ")

console.log(item);
console.log(item2);

