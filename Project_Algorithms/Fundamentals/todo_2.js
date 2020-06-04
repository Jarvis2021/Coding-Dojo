

//Countdown


// var arr = [];
// function newArray(x){
//   for (var i=x; i>=0; i--){
//
//     arr.push(i);
//   }
//  return arr;
// }
//
// var y = newArray(7);
// console.log(y);







// Print and Return

// function printReturn(a,b){
//   console.log(a);
//   return b;
// }
//
// var x = printReturn(1,3);
// console.log(x);


// First Plus Length


// function unKnownResult(x){
//      var i = 0;
//      var y = x.length;
//      var z = x[i] + y;
//      console.log(z);
//     }
//
//
// unKnownResult([1,2,5,7,9,0,10,11,12,13]);
// unKnownResult(["What",2,5,7,9,0,10,11,12,13]);
// unKnownResult([false,2,5,7,9,0,10,11,12,13]);
// unKnownResult([true,2,5,7,9,0,10,11,12,13]);





// Values Greater than Second  && Values Greater than Second, Generalized


// function counter(x){
//
//   var count = 0;
//
//   if(x.length <2)
//   {
//
//     return "Not a valid array";
//   }
//
//   for (var i=0; i<=x.length; i++)
//
//   {
//     if(x[i] > x[1])
//
//     {
//       console.log(x[i]);
//       count = count + 1;
//     }
//   }
//   return count;
// }
//
// console.log(counter([1,3,5,7,9,13]));
// console.log(counter([1]));





// Fit the First Value


function fitValue(x){

var i = 0;
var y = x.length;

if (x[i] > y){
  console.log("Too big!");
}

else if( x[i] < y){

  console.log("Too small!");
}

else {
  console.log("Just Right!");
}

}

fitValue([5,2,3]);
