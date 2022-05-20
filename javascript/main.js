// COMMENTS

/* 
this is a
multiline comment
*/

// PRINTING
console.log("hello world"); // an inline comment


// Data types (7). Types are dynamic i.e. types can change.
// undefined, null, boolean, string, symbol, number (both int & floats), object
var a; // declaring an undifined variable
a = 7; // assigning a to 7
var myName = 'Muzi'; // declaring a & assigning a variable. Used throught program
let myAge = 32; // only used in the context of declaration (block-level variables)
var isTrue = true; // boolean
const myGender = "Male"; // never changes

// numbers
3 / 2; // 1.5
Math.floor(3/2); // 1
parseInt('123', 10); // 123. 2nd arg is base conversion

// strings
'hello' + 'world'; // 'hello world'
'1' + 2 + '3'; // '123'
'hello'.reversed(); // 'olleh'
'hello'.length; // 5


// special values
1 / 0; // Infinity
-1 / 0; // -Infinity
null; // non-value
undefined; // uninitialized variable


// COLLECTIONS (Lists/Arrays, Maps/Dicts, Sets, Tuples, Enums)
// Arrays
var cars = ['VW', 'BMW', 'Toyota'];

// creating an array
const a = new Array();
a[0] = 'firstElement';

// array attributes and methods
a.length; // 1 (length is len + 1)
a.toString(); // returns a string for each element
a.push('item_to_append');

// FLOW CONTROL (If, For-loops, While, Switch, Tenary, Null-Aware)
// If Statement
if (10 > 2) {
    return "10 is greater than 2";
} else if (10 == 2) {
    return "10 is equal to 2";
} else {
    "10 is smaller than 2";
}


// ternary operator
const allowed = (age > 18) ? 'yes' : 'no';

// Switch Statement
switch(a) {
    case a == 3:
        break;
    case a == 7:
        break;
    default:
        // default is optional.
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
    console.log(i);
}

// for-in
// Loops through the properties of an object
var person = {fname: 'Muzi', lname: "Xaba", age: 32};
var text = "";
var x;
for (x in person) {
    text += person[x]; // loops through indecies
    console.log(text);
}

// for-of
// Loops through the values of an iterable
var myList = [1,2,3,4,5];
for (x of myList) {
    console.log(x);
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
// Comparison (==, ===[equal value & equal type],
// !=, !==[not equal valur or not equal type], ?[tenary operator])
123 == '123'; // true
1 == true; // true
123 === '123'; // false (type coercion)
1 === true; // false

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
    const total = a + b;
    return total;
}

// accessing all arguments within a function
function adder() {
    let sum = 0;
    for (const item of arguments) {
        sum += item;
    }
    return sum;
}
adder(1,2,3); // 6

function avg(...args) {
    let sum = 0;
    for (const item of args) {
        sum += item;
    }
    return sum / args.length;
}
avg (2,3,4,5); // 3.5

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

// creating an empty object
const obj = new Object();
const obj = {};


// Object prototypes and instances
function Person(name, age) {
    this.name = name;
    this.age = age;
    this.nameInCaps = function() {
        return this.name.toUpperCase();
    }
}

Person.prototype.emailAddress = function () {
    return this.first + "@email.com";
}

Person.prototype.toString = function () {
    return '<Person: ' + this.name + '>';
}

// defining a new object from prototype
const me = new Person('Muzi', 34);

// accessing object properties
const name = me.name; // 'Muzi'
const name = me['name']; // 'Muzi'

// built-in functions


// check Boolean
Boolean(13); // true
Boolean(''); // false

// convert a string into an integer/float
// Not-a-Number (NaN) returned if string can't be parsed
parseInt(), parseFloat(), + '22'

// test for NaNs
Number.isNaN('1'); // false



// String Properties & Methods
'string'.length;
'string'.charAt(0); // 's'
'hello, world'.replace('world', 'mars'); // 'hello, mars'
'string'.toUpperCase(); // 'STRING'
