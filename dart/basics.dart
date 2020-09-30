import 'dart:io';

import 'dart:svg'; // for stdout & stdin

void main () {
  print('this functions always gets run');
  print(myFullName("Muzi","Xaba"));

  stdout.writeln("What's your name: ?");
  String userName = stdin.readLineSync();
  print("The user's name is $userName");
}
// inline comment

/*
Block comment
*/

/// Documentation

/*
Dart is a static type & compiled OOP langauge
Everything is an object
Supports Ahead of time & Just-in-Time compilation
Strongly typed as variable types r known at compile time
Python & JavaScript are Dynamically Typed Languages.
Dynamically typed language vars are known at run time.

'int num;' is the same as 'int num = null;'
'var x2 = [...x];' making a deep copy of 'x' using the spread operator
}
*/

// Variable Types
String myName = "Muzi";
int age = 32;
double heightInMeters = 1.75;
bool isMale = true;
dynamic mayChangeTypes;
var anyType = "dart will infer the type";

// Constants & Final
// Const can only be used for top-level, static, local variables
final String userMood = """Run time constant.
                       Can assume new value everytime code is run""";
const String password = "Compile time constant. Implicitly 'final'.Will never change";

var foo = const []; // the object is const but the variable isn't
final bar = const []; // the variable is final & the object is const

// Collections
List<String> siblings = ['Velile', 'Nathi', 'Mini'];
Map<String, dynamic> user = {"username": "User", "age": 22, "height": 1.72};
Set<int> nums = {1,2,3,3,3,4,6,6};



// Strings
String myName2 = 'Muzi';
String aboutName = "dollar sign for string interpolation: $myName2";
String multilineString = """This is for
                      multiline strings""";
String rawString = r"Nothing will be \n escaped";
String lowerCaseName = myName2.toLowerCase(); // string method
int getStringLenght = myName2.length; // returns length of string as int
String ageAsString = age.toString(); // casting an int as String

// Integers
int shoeSize = 10;
int stringToInt = int.parse('1');
int a = ++shoeSize; // increaments shoeSize b4 assigning 'a' value
int b = shoeSize++; // increaments shoeSize after assigning 'b' value
b += 1;

// Doubles
double half = 0.5;
double fromString = double.parse("0.5");

// Operators
// -+/*
// % modulo
// num++ = num + 1
// &&, || for logical operators

// Tenary Operator
// condition ? "If true" : 'If false';
// Null Aware Operators
// '?.', '??', '??='
// '?.' Returns null is object before it is null
// 'a ??= 5' Will only assign a to 5 if a is null
// 'b ?? 6' Will return b if b is null, other wise it will return 6

// Spread Operator
//'var x2 = [...x];' making a deep copy of 'x'


// Getting user input
// stdout.writeln("What's your name: ?");
// String userName = stdin.readLineSync();
// print("The user's name is $userName");

// If Statements
if (shoeSize > 11 && age < 35) {
  print("You've got some big feet");
} else if (age > 21) {
  print("You're an adult");
} else {
  print("Just wear shoes");
}

// Switch Statement
int number = 3;
switch (number) {
  case 0:
    print("The number is 0");
    break;
  case 3:
    print("The numbe is 3");
    break;
  default:
    print("Couldn't find the number");
}

// For Loop
for (var i=1; i<=10; ++i) {
  print(i);
  //if (i%2==0) break/continue;
}

// For-in Loop
var nums = [1,2,3,4,5];
for (var n in nums) {
  print(n);
}

// For-Each Loop
numbers.forEach((n) => print(n));

// While Loop
while (shoeSize > 0) {
  print(shoeSize);
  shoeSize -= 1;
}

// Do-While Loop
do {
  print(shoeSize);
  shoeSize -= 1;
} while (shoeSize > 0)


// type return by function gets written infront of the function name
// {curly braces} for optional args
String myFullName (String firstName, String lastName) {
  return firstName + " " +lastName;
}

dynamic sum(var positionalArg, var positionalArg2) => positionalArg + positionalArg2;
dynamic sum2(var positionalArg, [var optionalPositionalArg]) {
  positionalArg + (positionalArg ?? 0);
  // if optionalPositionalArg null, make it 0
}
// named parameters r similar to python's kwargs. func(var1: #, var2: #) when calling
dynamic sum3({var namedParam, var namedParam2}) => namedParam + namedParam2;

// Assert. Similar to python's assert
assert(10 > 5);




// Classes
/**
 * The doc string for the Person class
 */

class Person {
  String name;
  int age;

  // static attribute. used for class level variable
  static const String nationality = 'South African';

  // constructor with optional positional argument
  Person(this.name, [this.age = 18]);

  // named constructor
  // Person guest = Person.guest();
  Person.guest() {
    name = 'Guest';
    age = 18;
  }

  void showOutput() {
    print(name);
    print(age);
  }
}
// Person p1 = Person(); create class instance 


// Looking at inheritance
class Vehicle {
  String model;
  int year;

  Vehicle(this.model, this.year);

  void showVehicleInfo() {
    print(model);
    print(year);
  }

  void showModelOnly() => print(model);
}

// Inheritance done using 'exends'
class Car extends Vehicle {
  double price;

  // get the instances year internally but model & year from parent
  Car(String model, int year, this.price) : super(model, year);

  void showCarInfo() {
    super.showVehicleInfo();
    print(this.price);
  }

  // Overiding parent method
  @override
  void showModelOnly() {
      print(this.price);
      print("Overriding the parent method");
  }

}

// creating an instance from a class that inherits from another
// Car car1 = Car('Jetta', 2013, '45000');
// Car.showCarInfo();


// Exceptions (try-catch)
/*
try {
  code that might throw an exception/error
} on SpecificError catch(e) {
  print(e);
}  catch (error) {
  print(error);
} finally {
  run this code no matter what
}
*/

// Throwing an Exception
/*
if (condition) {
  throw SpecificException("Message to return");
}
*/