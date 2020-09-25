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

// Types of js FOR LOOPS

// for
// for (1, 2, 3) {
    // code block
//}
// 1. executed once, b4 execution of code block
// 2. condition for executing the code block
// 3. executed every time after the code block executes
for (var i = 0; i < 10; i++) {
    print(i);
}

// for-in
// Loops through the properties of an object
var person = {fname: 'Muzi', lname: "Xaba", age: 32};
var text = "";
var x;
for (x in person) {
    text += person[x];
    print(text);
}

// for-of
// Loops through the values of an iterable
var myList = [1,2,3,4,5];
for (x of myList) {
    print(x);
}

// WHILE LOOPS

// Basic While Loop
/* while (condition) {
    // execute code block
}
*/
// Remember to add something to stop the looping

// Do While Loop
// will execute the code block once b4 checing the if the condition is true
var q = 5;
do {
    //code block
    print(q);
    q--;
} while (q < 0 );

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