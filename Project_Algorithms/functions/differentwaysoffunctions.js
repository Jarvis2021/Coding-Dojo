
//  Declaration Function

function sum(a,b) {
  return a+b;
}
console.log(sum(2,4));

// Expression function

  // Can be Named:

  (function sum(a,b) { return a+b;}); console.log(sum(3,5));

  // Assign to a Variable:

  var x = (function (a,b) { return a+b;});  console.log(x(3,4));

// Arrow Function

function *sum(a, b) { yield a + b; }
