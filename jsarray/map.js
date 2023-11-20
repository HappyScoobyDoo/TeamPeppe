const numbers = [1,-1,2,3];
/*
const mapped = numbers.map(n => '<li>' + n + '</li>');

const html = '<ul>' + mapped.join('') + '</ul>';
console.log(mapped);
console.log(html);
*/
/*
const mapped = numbers.map(n => {
    const obj = { value: n }
    return obj;
})
*/
const mapped = numbers.map(n => ({value: n}) )
console.log(mapped);

const words = ["paperino","pluto","gargamella","suca",4]
const item = words
.filter(n => typeof(n) === "string")
.map(n => ({word : n+"suca"}))
console.log(item)