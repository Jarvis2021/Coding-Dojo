// count of Odd Numbers in a given Array

let counter = 0;

let arrayofIntegers = [21,1,3,5,7,9,21,23,33,13,45,67]

arrayofIntegers.forEach((integer) => {
  const remainder = Math.abs(integer % 2);
  counter += remainder;

});

console.log(counter);
