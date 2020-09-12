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
const String userMood = """Run time constant.
                       Can assume new value everytime code is run""";
final String password = "Compile time constant. Will never change";

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


// Getting user input
// stdout.writeln("What's your name: ?");
// String userName = stdin.readLineSync();
// print("The user's name is $userName");

// Flow Control - If Statements
if (shoeSize > 11 && age < 35) {
  print("You've got some big feet");
} else if (age > 21) {
  print("You're an adult");
} else {
  print("Just wear shoes");
}

// type return by function gets written infront of the function name
String myFullName (String firstName, String lastName) {
  return firstName + " " +lastName;
}

// Assert. Similar to python's assert
assert(10 > 5);




// Classes
/**
 * The doc string for the Person class
 */
class Person {

}