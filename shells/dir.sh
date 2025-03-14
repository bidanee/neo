#!/bin/bash

# -d 디렉토리인지 아닌지 확인

if [ -d $1 ]; then
  echo "$1 Directory is exit~!!"
else
  echo "$1 Directory is not exit~!!"
fi

