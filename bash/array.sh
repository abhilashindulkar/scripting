#!/bin/sh

NAME[0]="Abhilash"
NAME[1]="Lana"
NAME[2]="Vinayak"
NAME[3]="Ram"
NAME[4]="Daisy"
echo "First Index: ${NAME[0]}"
echo "Second Index: ${NAME[1]}"
echo "Third Index: ${NAME[2]}"


echo "First Method: ${NAME[*]}"
echo "First Method: ${NAME[@]}"
