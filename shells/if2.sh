#!/bin/bash

echo "File Name : $0"
echo "Parameter Count : $#"
echo "All Parameter : $0"

if [ "$1" = "$2" ]; then
  echo same~!!
else
  echo not same~!!
fi
