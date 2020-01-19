                     // Arrays Reintroduction
//Given an array and a value Y, count and print the number of array values greater than Y.

function  greaterValueCount(x,y){
  var max = 0;
  var counter = 0;
  for (var i = 0; i<x.length; i++) {

    if (x[i] > y) {
      max = x[i];
      counter = counter + 1;
    }

  }
  return counter;
}

console.log(greaterValueCount([1,3,4,5,7,9,10],4));


// Given an array, print the max, min and average values for that array.

function maxMinAvg(x){
  var arr = [];
  var max =0;
  var min = 0;
  var sum =0;
  for (var i=0;i<x.length; i++){
    sum = sum + x[i]
    if (x[i]>max){
      max = x[i];
    }
    else if (x[i]<min){
      min = x[i];
    }
  }
    var avg = sum/x.length;
    arr.push(max);
    arr.push(min);
    arr.push(avg);
    return arr;
}

console.log(maxMinAvg([1,3,-2,10]))



// Given an array of numbers, create a function that returns a new array where negative values were replaced with the string ‘Dojo’.
//For example, replaceNegatives( [1,2,-3,-5,5]) should return [1,2, "Dojo", "Dojo", 5].

function resetArray(x){
  for (var i=0; i<x.length; i++){
    if(x[i]<0){
      x[i] = "Dojo";
    }
  }
  return x;
}

console.log(resetArray([1,2,-3,-5,5]));



//Given array, and indices start and end, remove vals in that index range, working in-place (hence shortening the array).
//For example, removeVals([20,30,40,50,60,70],2,4) should return [20,30,70].

function removeArrayValues(x,y,z){
  for(var i=0; i<x.length; i++){
    if (x[i]== y){
      x.splice(indiex,i);
    }
    else if (x[i] == z) {
      x.splice(indiex,i);
    }

  }
  return x;
}

console.log(removeArrayValues([20,30,40,50,60,70],2,4));
