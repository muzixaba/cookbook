console.log("helllo");

let age: number = 10;
if (age < 50) {
    age += 10;
}

let sales: number = 10_000_000;
let course: string = "TypeScript";
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
let arr2: number[] = [1, 2, 3];

// TS tuple
// fixed length array
let arr3: [number, string] = [1, '2'];

// TS enum
// enum is a set of named constants
enum Color { Red, Green, Blue }

// TS Function
function add(a: number, b: number, c = 2): number {
  if (c) {
    return a + b + c; 
}
return a + b;
}

// TS Function with Union type
function add2(a: number | string, b: number | string): number | string {
  // narrow down the type
  if (typeof a === 'string' || typeof b === 'string') {
    return a.toString() + b.toString();
  }
  return a + b;
}


// TS objects
type Person = {
  name: string;
  age: number;
  hobbies: string[];
  role: [number, string];
  email: (name: string) => string;
} 

let max: Person ={
  name: 'Max',
  age: 30,
  hobbies: ['Sports', 'Cooking'],
  role: [2, 'author'],
  email: ('Max') => {`name` + '@gmail.com'}
};


// TS Union type
type Draggable = {
  drag: () => void;
}

type Resizable = {
  resize: () => void;
}

type UIWidget = Draggable & Resizable;

let textBox: UIWidget = {
  drag: () => {},
  resize: () => {}
}

// TS Literal Types
// Literal types are types that are a subset of a string, number, or boolean literal type.
type Quantity = 50 | 100 | 150 | 200;
let quantity: Quantity = 50;

// TS Nullable Types
function greet(name: string | null | undefined) {
  if (name) {
    console.log(`Hello ${name.toUpperCase()}`);
  } else {
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
}
// Use ?. incase the property doesn't exist
let jobTitle = person?.job?.title;
console.log(jobTitle);