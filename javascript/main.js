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

// Scopes (Global, Module, Function, Block)
// var - function level scoped (avoid, most of time)
// const - block level scoped, immutable
// let - block level scoped, mutable

// numbers
3 / 2; // 1.5
Math.floor(3/2); // 1
parseInt('123', 10); // 123. 2nd arg is base conversion

// strings
'hello' + 'world'; // 'hello world'
'1' + 2 + '3'; // '123'
'hello'.reversed(); // 'olleh'
'hello'.length; // 5
'hello'.replace("l", "x"); // hexlo
'hello'.replaceAll("l", "x"); // hexxo
' world '.trim(); // 'world'
' world '.trimStart(); // 'world '
' world '.trimEnd(); // ' world'
'7'.padStart(3, '0'); // '007'
'yes'.padEnd(6, '!!!'); // 'yes!!!'

// special values
1 / 0; // Infinity
-1 / 0; // -Infinity
null; // non-value
undefined; // uninitialized variable

// Undefined or Null values
value.?prop // evaluates to undefined if value/prop is null/undefined
value ?? defaultValue // returns defualtValue if value is null/undefined

// NAMING CONVENTION
/*
camelCase - variables, function defs,
PascalCase - Class names,
ALL_CAPS - constants
*/

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

// array methods (for arrays of objects)
const people = [
                {name: "Muzi", age: 34},
                {name: "Nkanyezi", age: 3}
            ]

// FILTER - find elements that meet certain condition. Returns a new array
const adults = people.filter((person) => {
    return person.age > 18
});

// MAP - apply some transformation to all objects
const names = people.map((person) => {
    return person.name
});

// FIND - finds a single object in array
const foundName = people.find((person) => {
    return person.name === 'Nkanyezi'
});

// forEach
people.forEach((person) => {
    console.log(person.name)
});

// SOME - return true if one element meets condition. Similar to python's any()
const isYoungerThan16 = people.some((person) => {
    return person.age < 16
});

// EVERY - return true if every element meets condition. Similar to python's all()
const isOlderThan1= people.some((person) => {
    return person.age > 1
});

// REDUCE - Applies an operation(s) on the array and returns the combination. 2nd param is the starting total
const totalAge = people.reduce((currentTotal, person) => {
    return person.age + currentTotal
}, 0);

// INCLUDES - Checks membership of an element. Returns boolean
const nums = [1,2,3,4,5];
const includes2 = nums.includes(2);

// Shallow Copies
const objCopy = {...obj};

// Object Destructuring
const {a, ...remaining} = {a:1, b:2, c:3}; //remaining === {b:2, b:3}

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

// shorthand ternary operator
// if showAddTask is true, the AddTask component will be shown
{showAddTask && <AddTask onAdd={addTask} />}


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
for (let x in person) {
    text += person.x; // loops through indecies
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

/**
 * This function sums up two numbers
 * 
 * @param {number} a The first argument
 * @param {number} b The second argument
 * @returns {number} The sum of a and b
 */
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

// run a specific function after 5 seconds
setTimeout(customFunctionName, 5000); // customFunctionName is a callback
setTimeout(() => {console.log("CustomFunction")}, 5000); // Arrow function being used as a callback

// check Boolean
Boolean(13); // true
Boolean(''); // false

// convert a string into an integer/float
// Not-a-Number (NaN) returned if string can't be parsed
parseInt('22');
parseFloat('22');

// test for NaNs
Number.isNaN('1'); // false

// String Properties & Methods
'string'.length;
'string'.charAt(0); // 's'
'hello, world'.replace('world', 'mars'); // 'hello, mars'
'string'.toUpperCase(); // 'STRING'

// Plain Objects
const plainObj = {
    name: "Muzi",
    surname: "Xaba",
    heightInMeters: 1.8,
    getFullName(){
        return `${this.name} ${this.surname}`
    }
}

// CLASSES
class Person {
    constructor(name){
        this.name = name;
    }
    describe(){
        return `Person name is ${this.name}`;
    }
}

// JSDoc
npm install -g jsdoc

// Generate HTML version of documentation
// HTML page found inside out/global.html
jsdoc main.js



// DOM (Document Object Model)
/*
A represantation of your HTML as a JS object.
Represents HTML as a tree of nodes & elements

*/

// view the dom or any element(s)
console.log(document);
console.log({obj}) // shows object with its name and value
console.table(obj) // returns the element is table format
console.dir(obj)
console.trace()
console.assert(condition, "Assertion message")
console.error(condition, "Error message")
console.warning(condition, "Warning message")
console.time, console.timeEnd // time how long object(s) render

// view a DOM node
console.log(document.head);


// SELECTORS - getElementById("#theID")
var title = document.getElementById('header-title');

// SELECTORS - getElementsByClassName
var items = document.getElementsByClassName('class-name');

// SELECTORS - getElementsByTagName
var li = document.getElementsByTagName('li')

// SELECTORS - querySelector
// only selects the first item that matches selection
var header = document.querySelector('#id');

// select all elements that matche selection
var container = document.querySelectorAll('div');

// SELECTORS - querySelectorAll
// selects multiple items
var header = document.querySelector('.class-name');

// add HTML inside of a node
title.innerHTML = '<h3>New Title</h3>';

// change CSS style
title.style.borderBottom = 'solid 3px #000';


// Travesing the DOM
// Parent
// Child
// Sibling


// Parent Nodes
var listParent = document.parentNode;
var listParent = document.parentElement;

// Children
var itemList = document.children;
var itemList = document.firstElementChild;
var itemList = document.lastElementChild;

// Siblings
var sibling = itemList.nextSibling;
var sibling = itemList.previousSibling;
var sibling = itemList.nextElementSibling;
var sibling = itemList.previousElementSibling;


// EXPORTS //
// named exports
/*
Can be many from a single file
export {a, b, c}; // "my-module.js"
import {a, b, c} from './my-module.js';

*/

// default export
/*
Only one export per module
export default function square(x) {return x * x}; //"my-module.js"
import square from "./my-module.js"
*/


// LOCAL STORAGE //
// Allows the storing of key-values pairs in the browser
// Has no expiration date unless if user is browsing 'privately'
localStorage.setItem("name": "Muzi");
localStorage.getItem("name");



// ARRAY Destructuring
const alphabets = ['A', 'B', 'C', 'D', 'E'];
// get first 2 elements
const [a, b] = alphabets; // a=A, b=B
// get first & third elements only
const [a,, c] = alphabets; //a=A, c=C, rest=['D','E]
// get first, third, & rest of elements
const [a,, c, ...rest] = alphabets;


// OBJECT Destructuring
const personOne = {
    name: "Sally",
    age: 32,
    address: {
        city: "Durban",
        province: "KZN"
    }
}

const { name, age, address: {city, province} } = personOne;


// REGEX (regular expressions)

// Username must be 6-8 chars long & be alphanumeric
const usernamePattern = /^[\w]{6,8}$/i;

// Use pattern.text() to check if regex found in string
usernamePattern.test("Muzi1234") // true
usernamePattern.test("Muzi12345678") // false


emailPattern = /^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$/

console.log(emailPattern.test("muzi123@Gmail.com"));
console.log(emailPattern.test("muzi.xaba@Gmail.co.za"));

