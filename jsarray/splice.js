//delete element
let names = ['Danni','Joe','Sarah','Molly','Thomas','Lucas'];
let nameCopy = [...names];
let nameCopies = [...names];
let splice = names.splice(1,3)
nameCopy.splice(1,4)
console.log(names)
console.log(splice)
console.log(nameCopy)
//delete and replace
nameCopies.splice(1,2, 'Bill', 'Bob')
console.log(nameCopies)