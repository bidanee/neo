#!/bin/bash

# 옛날에 쓰던 파일? 휴가갈때 썼었다고 함
# -f는 파일인지 확인하는 거임

if [ -f /home/$1/.plan ]; then
  cat /home/$1/.plan
else
  echo "User $1 is not make .plan file."
fi