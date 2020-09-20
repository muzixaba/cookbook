// COMMENTS

/* 
this is a
multiline comment
*/

// PRINTING
console.log("hello world"); // an inline comment


// Data types (7). Types are dynamic i.e. types can change.
// undefined, null, boolean, string, symbol, number (both int & floats), object
var a; // declaring a variable
a = 7; // assigning a to 7
var myName = 'Muzi'; // declaring a & assigning a variable. Used throught program
let myAge = 32; // only used in the context of declaration
const myGender = "Male"; // never changes
var isTrue = true; // boolean


// COLLECTIONS (Lists/Arrays, Maps/Dicts, Sets, Tuples, Enums)
// Arrays
var cars = ['VW', 'BMW', 'Toyota'];


// FLOW CONTROL (If, For-loops, While, Switch, Tenary, Null-Aware)
// If Statement
if (10 > 2) {
    return "10 is greater than 2";
} else if (10 == 2) {
    return "10 is equal to 2";
} else {
    "10 is smaller than 2";
}

// Switch Statement
switch(a) {
    case a == 3:
        break;
    case a == 7:
        break;
    default:
        // defaul can be excluded.
        // if included, it will run if the other cases don't
        a == 10;
}

//TODO: Add for loops

// OPERATORS (Comparison, Arithmetic, Logical, Assignment, Bitwise, Identity, Membership)
// Comparison (==, ===[equal value & equal type], !=, !==[not equal valur or not equal type], ?[tenary operator])
// Arithmetic (+, -, *, /, %, ++, --)
// Logical (&&, ||, ![not])
// Assignment (=, +=, -=, **=)
// Bitwise (&, |, ~[not], ^[xor])
// Identity/Type (typeof, instanceof)
typeof "Must return string"
// Membership ()

// FUNCTIONS
// defined with 'function' keyword followed by function name, then ()
function funcName(a, b) {
    return a + b;
}

// ERROR/EXCEPTION HANDLING


// OBJECT ORIENTED PROGRAMMING
// Objects are python dict style with name:value pairs called properties
// Properties are written like variable names
// Can retrieve property value in objName.propertyName or objName['propertyName']
// Access an object's method objName.methodName/propertyName
var person = {
    fname: 'Muzi', 
    lname: 'Xaba', 
    age: 33, 
    eyeColour: 'brown',

    // object method
    fullName: function(){
        return this.fname + " " + this.lname;
    }
};