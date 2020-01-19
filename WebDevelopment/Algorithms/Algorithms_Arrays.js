//Return the given array, after setting any negative values to zero. 
//For example resetNegatives( [1,2,-1, -3]) should return [1,2,0,0].

    function resetNegatives(x){
        for (var i = 0; i<x.length; i++){

            if (x[i] < 0) 
            {
                x[i] = 0;
            }
        }
        return x;
    }
    y = resetNegatives([1,2,-1,-3]);
    console.log(y);

    // Given an array, move all values forward by one index, dropping the first and leaving a ‘0’ value at the end.  
    // For example moveForward( [1,2,3]) should return [2,3,0].

    function resetArray(x){

        for (var i=0; i<x.length; i++){
           
            x[i] = x[i+1];
        }

        x[x.length-1] = 0;
        return x;

    }
    
    y = resetArray([1,4,6,7,8,3]);
    console.log(y);



// Given an array, return an array with values in a reversed order.  For example, returnReversed([1,2,3]) should return [3,2,1].

function reverseofArray(x){
    var arr = [], count = 0;
    for (var i = x.length-1; i >= 0; i--) {
        arr[count] = x[i];
        count += 1;
    }
    return arr;
}

console.log(reverseofArray([1,2,3,4,5]));


//

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
  

