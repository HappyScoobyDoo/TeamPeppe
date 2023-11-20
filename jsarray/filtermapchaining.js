const numbers = [1,-1,2,3];

const items = numbers
.filter(value => value > -1)
.map(n => ({value: n}))
.filter(obj => obj.value > 1)
.map(obj => obj.value*2);

console.log(items);