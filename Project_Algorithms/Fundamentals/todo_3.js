// Biggie Size


function makeitBig(arr){
  for (var idx = 0; idx<=arr.length; idx++){
    if (arr[idx] > 0){
      arr[idx] = "big";
    }
  }
 return arr;
}

// console.log(makeitBig([-1,3,5,-5]));


// Print Low, Return High


function printLowHigh(arr)
{
  var min = arr[0];
  var max = arr[0];

  for (var i=0; i< arr.length; i++){

    if (arr[i] < min)
    {
      min = arr[i];
    }
    if (arr[i] > max)
    {
      max = arr[i];
    }
  }
  console.log(min);
  return max;
}

// console.log(printLowHigh([-1,3,-7,5,-5,10]));




// Print One, Return Another

function printOneReturn(arr){
  var x = (arr.length) - 2;
  console.log(arr[x]);
  for (var i= 0; i<arr.length; i++){

    if ( arr[i]%2 !=0){

      return arr[i];
    }

    else {

      continue;
    }
  }
}

// console.log(printOneReturn([0,7,3,1,3,-7,5,-5,10,11,8]));



// Double Vision

function doubleArray(arr){
  for ( var i = 0; i< arr.length; i++){
    arr[i] = arr[i] * arr[i];

  }
  return arr;
}

// console.log(doubleArray([1,2,4,6]));



// Count Positives


function countPositives(arr){
  var count = 0;
  for (var i=0; i<arr.length; i++)
  {
    if (arr[i]>0)
    {
      count = count + 1;
    }
  }
  arr[arr.length-1] = count;
  return arr;
}

// console.log(countPositives([-1,1,1,1,1]));


//  Evens and Odds


function evenOdds(arr){
  for (var i= 0; i<arr.length; i++)
  {

    if (arr[i]%2 !=0 && arr[i+1]%2 !=0  && arr[i+2]%2 !=0)
    {
      console.log("That's Odd!");
    }
    else if (arr[i]%2 ==0 && arr[i+1]%2 ==0  && arr[i+2]%2 ==0)
    {
      console.log("Even More So!!");
    }
  }
}

// evenOdds([2,4,3,6,1,5,3,2,5,6,7,8]);



// Increment the Seconds

function incrOddElem(x)
{
  for (var i=0; i< x.length; i++)
  {
    if (i%2 !=0){
      x[i] = x[i] + 1;
      console.log(i, x[i]);
    }
  }
  return x;
}

// console.log(incrOddElem([0,1,4,5,8,9,12,13,16,17,20,21]));





//  Previous Lengths


function prevLength(x)

{


  for (var i=1; i<x.length; i++)

  {
    var temp = x[i+1];
    x[i] = x[i-1].length;

  }

  return x;
}

// console.log(prevLength(["Earnings","Michael","Clark", "Sophie"]));
