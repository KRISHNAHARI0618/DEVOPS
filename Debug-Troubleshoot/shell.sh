#! /bin/bash

myFunc(){
  echo "\$1 is $1"
  echo "\$2 is $2"
  a = "Goodbye Cruel"
  b = "hello"
}

a=hello
b=World

myFunc $a $b
echo "a is $a"
echo "b is $b"

