
// Part 1:

// Sigma :  Implement function sigma(num) that, given a number, returns the sum of all positive integers up to the given number (inclusive).  Ex: sigma(3) = 6 (or 1+2+3); sigma(5) = 15 (or 1+2+3+4+5).

// function sigma(x){
//   var sum = 0;
//   for (var i=0; i<=x; i++){
//     sum = sum + i;
//   }
//   return sum;
// }
// console.log(sigma(5));

// Factorial - Write a function factorial(num) that, given a number, returns the product (multiplication) of all positive integers from 1 up to the given number (inclusive).

// function factorial(x){
//   var fac = 1;
//   for (var i=1; i<=x; i++){
//     fac = fac * i;
//   }
//   return fac;
// }
// console.log(factorial(10));

// Array: Second-to-Last: Return the second-to-last element of an array. Given [42, true, 4, "Liam", 7], return "Liam".  If array is too short, return null.

// function returnSecondLast(x){
//   for (var i=0; i<x.length; i++){
//     if (x.length >=2) {
//       return x[x.length-2];
//     }
//     else {
//       return null;
//     }
//   }
// }
// console.log(returnSecondLast([7,2,3]));

//Array: Nth-to-Last: Return the element that is N-from-array's-end.  Given ([5,2,3,6,4,9,7],3), return 4.  If the array is too short, return null.


// function returnNthLast(x,y){
//   for (var i=0; i<x.length; i++){
//     if (x.length >=y) {
//       return x[x.length-y];
//     }
//     else {
//       return null;
//     }
//   }
// }
// console.log(returnNthLast([7,2,3],1));

//Array: Second-Largest: Return the second-largest element of an array. Given [42,1,4,3.14,7], return 7.  If the array is too short, return null.

// function secondLargestNum(x) {
//   var max = 0;
//   var secondmax=0;
//   for (var i=0; i<x.length; i++)
//   {
//     if (x[i] > max)
//     {
//       max = x[i];
//     }
//   }
//   //console.log(max);
//   for(var i=0; i<x.length; i++){
//     if (x[i] > secondmax && x[i] != max){
//       secondmax = x[i];
//     }
//   }
//   return secondmax;
// }
//
// console.log(secondLargestNum([43,42,1,4,44,3.14,7,54]));

// function secondLargestNumber(x){
//   var max = x[0];
//   var secmax = x[0];
//   for (var i=0; i<x.length; i++){
//     if (x[i] > max) {
//        max = x[i];
//     }
//     else if (x[i] > secmax && x[i]!=max) {
//       secmax = x[i];
//     }
//   }
//   return secmax;
// }
//
// console.log(secondLargestNumber([43,242,199,4,144,3.14,57,54]));


// function mirrorArrayValues(x){
//   var temp = [];
//   for (var i=1; i<x.length; i+2=){
//     x[i] = x.push(temp[i-1]);
//   }
//   return x;
// }
//
// console.log(mirrorArrayValues( [4, "Ulysses", 42, false


var tArr = ["One","Two","Three"];
var tList = tArr.join();

console.log(tList);
