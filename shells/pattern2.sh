#!/bin/bash

str="AAABBBCCC"
echo "${str##A*B}"

# ##:에서 시작해서 B로 끝나는