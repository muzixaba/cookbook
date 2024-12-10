"use strict";
var _a;
console.log("helllo");
// let age: number = 10;
// if (age < 50) {
//     age += 10;
// }
let sales = 10000000;
let course = "TypeScript";
let level; // any
// Javascript types
// number
// string
// boolean
// null
// undefined
// object
// symbol
// Additional TypeScript types
// any - declared but uninitialized variables
// unknown - used when you don't know the type of a variable
// void
// never
// enum
// tuple
// JS array
let arr = [1, 2, '3'];
// TS array
let arr2 = [1, 2, 3];
// TS tuple
// fixed length array
let arr3 = [1, '2'];
// TS enum
// enum is a set of named constants
var Color;
(function (Color) {
    Color[Color["Red"] = 0] = "Red";
    Color[Color["Green"] = 1] = "Green";
    Color[Color["Blue"] = 2] = "Blue";
})(Color || (Color = {}));
// TS Function
function add(a, b, c = 2) {
    if (c) {
        return a + b + c;
    }
    return a + b;
}
// TS Function with Union type
function add2(a, b) {
    // narrow down the type
    if (typeof a === 'string' || typeof b === 'string') {
        return a.toString() + b.toString();
    }
    return a + b;
}
let max = {
    name: 'Max',
    age: 30,
    hobbies: ['Sports', 'Cooking'],
    role: [2, 'author'],
    email: (name) => `${name}@gmail.com`
};
let textBox = {
    drag: () => { },
    resize: () => { }
};
let quantity = 50;
// TS Nullable Types
function greet(name) {
    if (name) {
        console.log(`Hello ${name.toUpperCase()}`);
    }
    else {
        console.log(`Hello`);
    }
}
// TS Optional proerty access operator
// ?. is called the optional chaining operator
// ?. is used to access properties of a nested object
let person = {
    name: 'Max',
    age: 30,
    job: {
        title: 'CEO',
        company: 'Google'
    }
};
// Use ?. incase the property doesn't exist
let jobTitle = (_a = person === null || person === void 0 ? void 0 : person.job) === null || _a === void 0 ? void 0 : _a.title;
console.log(jobTitle);
//# sourceMappingURL=index.js.map