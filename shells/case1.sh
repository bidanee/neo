#!/bin/bash

a=0

echo -n "Input : "
read a

let a/=10 
# 복잡한거 단순화 시키는 작업

case $a in
  10) echo "A";;
  9) echo "A";;
  8) echo "B";;
  7) echo "C";;
  6) echo "D";;
  *) echo "E";;
esac

echo "Thank you ~ Bye!1"