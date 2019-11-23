import 'dart:io';
import 'dart:async';

void main() {
  stdout.write("What is your name?\r\n");
  String name = stdin.readLineSync();
  print(name);
}