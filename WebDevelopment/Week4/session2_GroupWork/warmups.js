/* Build a function that prints all numbers from 1 to 255 */

function printNumbers (num) {
  for (var i = 0; i <= num; i++) {
    console.log(i);
  }
}

// printNumbers(255);

 /* Build a function that prints all evens from 1 to 255 */

 function printEvenNumbers(num){
   for (var i=1; i<=num; i++){
     if(i%2==0){
       console.log(i);
     }
   }
 }

// printEvenNumbers(255);

/* Build a function that accepts an array, iterates over the array and prints its values */

function printArrayValues(arr){
  for (var i=0; i<arr.length; i++){
    console.log(arr[i]);
  }
}

// printArrayValues([1,3,4,5,6,74,3,34,54]);

/* Build a function that accepts an array, replacing any values evenly divisible by 7 with "Lucky". Return tha array */

function replaceArrayValues(arr) {
  for (var i = 0; i < arr.length; i++) {
    if (arr[i]%7==0){
      arr[i] = "Lucky" ;
    }
  }
  return arr;
}

// console.log(replaceArrayValues([2,42,14,6,7,84,35,5]));