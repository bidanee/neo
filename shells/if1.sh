#!/bin/bash

echo "File Name : $0"
echo "Parameter Count : $#"
echo "All Parameter : $0"

if [ "$1" = ok ]
then
  echo good~!!
else
  echo bad~!!
fi
