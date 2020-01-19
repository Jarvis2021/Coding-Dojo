// Biggie Size :  Given an array, write a function that changes all positive numbers in the array to the string "big".
//Example: makeItBig([-1,3,5,-5]) returns that same array, changed to [-1, "big", "big", -5].


function positiveToBig(x){
  for (var i=0; i<x.length; i++){
    if (x[i] > 0){
      x[i] = "big";
    }
  }
  return x;
}

console.log(positiveToBig([-1,3,5,-5]));

// Print Low, Return High - Create a function that takes in an array of numbers.
//The function should print the lowest value in the array, and return the highest value in the array

function printLowreturnHigh(x){
  var max = 0;
  var min = 0;
  for (var i=0; i<x.length; i++){
    if (x[i] < min) {
      min = x[i];
    }
    else if ( x[i] > max){
      max = x[i];
    }
    }
    console.log(min);
    return max;
  }

printLowreturnHigh([-1,3,8,-5,-10]);
console.log(printLowreturnHigh([-1,3,8,-5,-10]));

// Print One, Return Another.  Build a function that takes in an array of numbers.
//The function should print the second-to-last value in the array, and return the first odd value in the array

function printOneReturnAnother(x){
  console.log(x[x.length-2]);
  for (var i=0; i<x.length; i++){
    if (x[i]%2 != 0) {
      var odd = x[i];
      return odd;
    }
  }

}
printOneReturnAnother([0,8,4,7,8,-5,-10,-11,-20,30]);
console.log(printOneReturnAnother([0,8,4,7,8,-5,-10,-11,-20,30]));


// Double Vision - Given an array (similar to saying 'takes in an array'), create a function that returns a new array where each value in the original array has been doubled.
//Calling double([1,2,3]) should return [2,4,6] without changing the original array.

function DoubletheArray (x){
  var newarray = [];
  for (var i=0; i<x.length; i++){

    newarray.push( 2 * x[i]);
  }
console.log(x);
return newarray;
}
console.log(DoubletheArray([-1,3,5,-5]));

// Count Positives - Given an array of numbers, create a function to replace the last value with the number of positive values found in the array.
//Example, countPositives([-1,1,1,1]) changes the original array to [-1,1,1,3] and returns it.

function countPositives(x){
  var count = 0;
  for (var i=0; i<x.length; i++){
    if (x[i] > 0){
      count = count + 1;
    }

  }
  x[x.length-1] = count;
  return x;
}

console.log(countPositives([-1,3,5,7,-5]));

// Evens and Odds - Create a function that accepts an array.  Every time that array has three odd values in a row, print "That's odd!".
//Every time the array has three evens in a row, print "Even more so!".

function evenOdds(x){
  var oddcount = 0;
  var evencount = 0
  for (var i=0; i<=2; i++){
    if (x[i] %2 !=0) {
    oddcount = oddcount +1;
    }
    else if (x[i]%2 == 0) {
      evencount = evencount + 1;
    }
  }
  if ( oddcount == 3) {
    console.log("That's Odd!")
  }
  else if (evencount == 3) {
    console.log("Even more so!")
  }
}
evenOdds([1,3,5,6,8]);
evenOdds([2,4,8,3,5,6,8]);
evenOdds([2,3,4,8,3,5,6,8]);


// Add Seven - Build a function that accepts an array. Return a new array with all the values of the original, but add 7 to each.
//Do not alter the original array.  Example, addSeven([1,2,3]) should return [8,9,10] in a new array.

function addSeven (x){
  var newarray = [];
  for (var i=0; i<x.length; i++){

    newarray.push(x[i] + 7);
  }
console.log(x);
return newarray;
}
console.log(addSeven([1,2,3,4]));

// Outlook: Negative Given an array, create and return a new one containing all the values of the original array, but make them all negative

function outlookNegative (x){
  var newarray = [];
 for (var i=0; i<x.length; i++)
 {
   if (x[i]>0)
   {
     x[i] = x[i] * -1;
   }
   newarray.push(x[i]);
 }
 return newarray;
}

console.log(outlookNegative([-1,2,3,4]));

//Always Hungry: Create a function that accepts an array, and prints "yummy" each time one of the values is equal to "food".  If no array values are "food", then print "I'm hungry" once

function amIhungry(x){
  for (var i = 0; i<x.length; i++){
    if (x[i] === "food"){
      console.log("yummy");
    }
    else {
      console.log("I'm hungry");
    }
  }
}

amIhungry(['food','nothungry', 'food']);

//Swap Toward the Center.

function swapCenter(x){
    for (var i = 0; i < x.length/2; i+=2){
        var temp = x[i];
        x[i] = x[x.length-i-1];
        x[x.length-i-1] = temp;
    }
    return x;
}

console.log(swapCenter([1,2,3,4,5]));


//Scale the Array.Given an array arr and a number num, multiply all values in the array arr by the number num, and return the changed array arr.
//For example, scaleArray([1,2,3], 3) should return [3,6,9].

function scaleArray(x,y){
  for (var i=0; i<x.length; i++){
    x[i] = x[i] * y;
  }
  return x;
}
console.log(scaleArray([1,2,3],3));




// ReverseArray:Given an array, write a function that reverses its values, in-place.  Example: reverse([3,1,6,4,2]) returns the same array, but now contains values reversed like so... [2,4,6,1,3]


function ReverseArray(x){

  for (var i=0; i<x.length/2; i++) {
    var temp = x[i];
    x[i] = x[x.length-1-i];
    x[x.length-1-i] = temp;
  }
  return x;
}
console.log(ReverseArray([1,3,5,6,8,9]));


// Increment the Seconds - Given an array of numbers arr, add 1 to every other element, specifically those whose index is odd (arr[1], arr[3], arr[5], etc).
// Afterward, console.log each array value and return arr.

function incrementSeconds(x){

    for ( var i=0; i<x.length; i++){
      if (i%2 !=0) {
        x[i] = x[i] +1;
      }
    }
    return x;
}
console.log(incrementSeconds([1,2,3,4,5]));
