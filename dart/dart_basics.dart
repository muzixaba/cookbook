//==========
// Intro
//==========

/// Created by Google.
/// Object oriented.
/// C styled - Similar to C, Java, JS, Swift
/// Statistically typed 
///     - Data types known at runtime.
///     - Once a variable has been assigned a type, it has to /// stay that way.
/// Can run on mobile and web.
/// Compiled to machine code.
/// Can compile to JavaScript using dart2js compliler
/// file extension = .dart

//===========================
// Basics
//===========================

void main(){
    //Everything inside here will run
    String name = 'Muzi'; //Semicolon to terminate lines
    print("hello, i'm $name); // $ to reference variables
    func_name(var_type arg1, var_type arg2);
}

//===========================
// Variables
//===========================

var_type var_name = value;
String name = 'Muzi';
int age = 31;
double height = 1.75;
var any_var = value; // dart will figure out the type at runtime
final constant_var = value; //final is used for constants
dynamic var_name = value; //allows a var type to change
null = no value

only mention the type of variable at creation.

-----------------------------------------------------------
// Calling variables
$var_name

------------------------------------------------------------
// Data types
String, int, double, bool, dynamic

------------------------------------------------------------
// Strings
character sequences
"double" or 'single' quotes
print("My name is ${name.length} letters long");
------------------------------------------------------------

//===========================
// Booleans
//===========================
true
false

//===========================
// Functions
//===========================
void func_name(String name, int age, double height){
    ///tripple slash for doc strings
    //void states function doesn't return anything. void is not required
}

String func_name(String name, int age, [double height=2.22]){
    //String states function returns a string
    // optional/default params inside []
    return "Hello, my name is $name, I'm $age yrs old and $heightm tall"
}

String func_with_named_vars({String name, int age, double height=2.22}){
    // {} is for named params. similar to kwargs in python
    // [] not allowed when you have {}
    // call_func_with_named_vars(name: 'value', age: #, height: #); 
    return "Hello, my name is $name, I'm $age yrs old and $heightm tall";
}

// Use arrow operator for one line funcs. think lambda
String say_name(String) => "Hi, my name is $name";
List<int> list_func() => [1,2,3]; // func will only return a list of integers

// Named functions == Normal functions
void funcName () {...}

// Anonymous Functions
() P{...}

//===========================
// Classes
//===========================

class Person {
    // Construct is same name as class. this==self in python
    Person({this.name, this.age, this.height}); 
    // Always declare var types in Classes
    final String name; // mark var as final for it to be immutable
    int age;
    double height;

    // class methods
    String describe(){
        return "Hello, I'm $name, I'm $age yrs old and $height meters tall";
    }
    Sring say_name() => "My name is $name"

    @override
    String toString() => "name: $name"; //overiding the toString method
}

// Inheritance. All objects inherit from Object
class Employee extends Person{
    Employee({String name, int age, double height, this.taxCode, this.salary})
        : super(name:name, age:age, height:height);
    final String taxCode;
    final int salary;
}

// abstract Classes
abstract class Shape {
    double area();
}
class Square implements Shape {
    Square({this.side});
    final double side;
    double area() => side * side;
}

import 'dart:math';

class Circle implements Shape {
    Circle({this.radius});
    final double radius; //stored property
    double area() => radius * radius * pi; //import pi from math module
}

// creating an interface from an abrstract class
void printArea(Shape shape) {
    print(shape.area());
}
voide printArea2(Shape shape) {
    double get area; //computed property. getter
}
void printArea2(Shape shape) {
    print(shape.area);
}

// Declare instance of class
final person = Person(name:'Muzi', age:31, height:1.75);
final employee = Employee(name:"Sbu", age:22, height:2.0, taxCode:'MS123', salary:4000);
print(employee.name); // accessing attributes
print(employee.say_name()); // accessing class methods
print(employee.toString()); // class string method

final square = square(side:5.0);
print(square.area());
printArea(squre); //using abstract class interface


//===========================
// Collections
//===========================

//--------Lists-------------
var my_list = [1,2,3];
my_list.add(88); // add==append in python
my_list.addAll([4,5,6]); //addAll is similar to extend in python
var empty_list = List(); // [] can take any data types
var empty_num_list = List<int>(); // can only take in integers

//--------Maps/Dicts--------------
var person = {'name':'Muz', 'age':36, 'height':1.78};
print(person['name']);
var new_map = Map<String, dynamic>();


//===========================
// Control Flow
//===========================

//--------If/Else--------------
if (conidition) {
    //do this
} esle if (another_condition) {
    //do the this thing
} else {
    // when all else fails
}
// if/else using a ternary operator.
// condition ? exprT : exprF
final type = (value % 2 == 0) ? 'even' : 'odd';
 
//--------While Loops--------------
int sum(List<int> values) {
    int i = 0;
    int result = 0;
    while (i < values.length) {
        result += values[i];
        i++;
    }
    return result;
}


//--------For Loops--------------
int sum(List<int> values) {
    int result = 0;
    for (int value in values) {
        result += values;
    }
    return result;
}
// also possible write one line Closures for for-loops.
// Closure is a function without a name.

//--------Switch Statements--------
enum NetworkError {
    badUrl,
    timeout,
    resourceNotAvailable,
}

void printError(NetworkError error) {
    switch (error) {
        case NetworkError.badUrl:
            print('bad url');
            break;
        case NetworkError.timeout:
            print('timeout');
            break;
        case NetworkError.resourceNotAvailable:
            print('resource Not Available');
            break;
    }
}

//===========================
// Imports
//===========================

//------Import Core Library------
import 'dart:math';

//-----Import library from external package-------
import 'package:test/test.dart';

//--------Import files-----------
import 'path/to/file_name.dart';

