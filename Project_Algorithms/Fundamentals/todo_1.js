
// Setting and Swapping

var myNumber = 42;
var myName = "Pramod";
var temp = myNumber;
myNumber = myName;
myName = temp;
console.log(myNumber);
console.log(myName);


// Print -52 to 1066

for(var i=-52; i<=1066; i++){

  console.log(i);
}


// Don’t Worry, Be Happy


function beCheerful(){
  console.log("good morning");
}

for(var i=1; i<=98; i++){
  console.log(i);
  beCheerful();
}


// Multiples of Three – but Not All

for (var i=-300; i<=0; i++){

  if(i== -3 || i == -6){
    continue;
  }
  else {
    if (i%3==0){
      console.log(i);
    }

  }

}



// Printing Integers with While

var i=2000;

while (i<=5280){

  console.log(i);
  i++

}



// You Say It’s Your Birthday

function myBirthday(x,y) {

  if (x==2 && y==3 || x==3 && y==2){

      console.log("How did you know?");
  }
  else {
    console.log("Just another day")
  }
}

myBirthday(3,2);


// Leap Year

function leapYear(x){

 if (x % 4 === 0 && x % 100 != 0 || x % 400 === 0){

   console.log("Its a leap year:", x)
 }

 else {
   console.log("Its not a leap year")
 }

}

leapYear(2020);



// Print and Count

  var count = 0;

  for( var i=512; i<=4096; i++){
    if (i%5 ===0) {
        console.log(i);
        count = count + 1;
      }
  }
  console.log(count);



// Multiples of Six

var i = 6;

while (i<=60000){

  if (i % 6 == 0){
    console.log(i);
  }
  i++;
}




// Counting, the Dojo Way

for(var i=1; i<=100; i++){

 if (i%10 == 0 &&  i %5 == 0){
   console.log('Dojo');
 }
 else if (i%5 == 0 && i %10 != 0){
   console.log("Coding");
 }
 else {
   console.log(i);
 }

}


//  What Do You Know?

function inputParam(incoming){

  console.log(incoming);
}

inputParam("Hello World");



// Whoa, That Sucker’s Huge…

var sum = 0;
for (var i=-300000; i<=300000; i++){
  sum = sum + i;
}
console.log(sum);




// Countdown by Fours


var i = 2016;

while (i>0){

  console.log(i);
  i = i-4;
}


// Flexible Countdown

var lowNum = 2;
var highNum = 9;
var mult = 3;

for (lowNum; highNum > 0;highNum--){
  if (highNum%mult == 0){
    var print = highNum
    console.log(print);
  }
}



// The Final Countdown

function givenP(a,b,c,d){

while (b<c){

  if (b%a == 0 &&  b!=d){
    console.log(b);
  }
  b++;
}

}

givenP(3,5,17,9);
