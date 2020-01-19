
Total Correct Values Predicted - 13 out of 15

------------------------------------------------------------------
function a(){
    return 35;
}
console.log(a())

Predicted Output : 35

Actual Output : 35

--------------------------------------------------------------------

function a(){
    return 4;
}
console.log(a()+a());

Predicted Output : 8

Actual Output : 8

--------------------------------------------------------------------

function a(b){
    return b;
}
console.log(a(2)+a(4));

Predicted Output : 2b

Actual Output : 6

--------------------------------------------------------------------

function a(b){
    console.log(b);
    return b*3;
}
console.log(a(3));

Predicted Output : 3,9

Actual Output : 3,9

--------------------------------------------------------------------

function a(b){
   return b*4;
   console.log(b);
}
console.log(a(10));

Predicted Output : 40

Actual Output : 40

--------------------------------------------------------------------

function a(b){
    if(b<10) {
        return 2;
    }
    else     {
        return 4;
    }
    console.log(b);
}
console.log(a(15));

Predicted Output : 4

Actual Output : 4

--------------------------------------------------------------------
function a(b,c){
    return b*c;
}
console.log(10,3);
console.log( a(3,10) );

Predicted Output : 10,3 ; 30

Actual Output : 10,3 ; 30

--------------------------------------------------------------------

function a(b){
    for(var i=0; i<10; i++){
        console.log(i);
    }
    return i;
}
console.log(3);
console.log(4);

Predicted Output : 3,4

Actual Output : 3,4

--------------------------------------------------------------------

function a(){
    for(var i=0; i<10; i++){
        i = i +2;
        console.log(i);
    }
}
a();

Predicted Output : 2,3,5,7,9,11

Actual Output  2,5,8,11

--------------------------------------------------------------------

function a(b,c){
    for(var i=b; i<c; i++) {
       console.log(i);
   }
   return b*c;
}
a(0,10);
console.log(a(0,10));


Predicted Output : 0,1,2,3,4,5,6,7,8,9 ;  0,1,2,3,4,5,6,7,8,9, - 0

Actual Output : 0,1,2,3,4,5,6,7,8,9 ;  0,1,2,3,4,5,6,7,8,9, - 0

--------------------------------------------------------------------

function a(){
    for(var i=0; i<10; i++){
       for(var j=0; j<10; j++){
           console.log(j);
       }
       console.log(i);
    }
}

Predicted Output : no output since the function is not called

Actual Output : No Output Value

--------------------------------------------------------------------

function a(){
    for(var i=0; i<10; i++){
        for(var j=0; j<10; j++){
            console.log(i,j);
        }
        console.log(j,i);
    }
}

Predicted Output : no output since the function is not called

Actual Output : No Output Value

--------------------------------------------------------------------


var z = 10;
function a(){
    var z = 15;
    console.log(z);
}
console.log(z);

Predicted Output : 10

Actual Output : 10

--------------------------------------------------------------------

var z = 10;
function a(){
    var z = 15;
    console.log(z);
}
a();
console.log(z);

Predicted Output : 15 , 10

Actual Output : 15, 10

--------------------------------------------------------------------

var z = 10;
function a() {
    var z = 15;
    console.log(z);
    return z;
}
z = a();
console.log(z);

Predicted Output : 15 , 15

Actual Output : 15, 15

--------------------------------------------------------------------
