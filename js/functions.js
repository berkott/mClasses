crazy("dude");

// Function Declaration
function crazy(word) {
    console.log(word);
}

let joe = crazy;

joe("joe");

// Function expression
let amazing = function(param) {
  console.log(param);
};

amazing("hello");

// Convenient arrow function
let quadratic_formula = (a, b, c, x) => a*x**2 + b*x + c;

console.log(quadratic_formula(1, 2, 3, 2));

let cool = (a, b, c, x) => {
    return a*x**2 + b*x + c;
};
