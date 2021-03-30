#!/bin/bash

NAME=abhilash

echo "$NAME"

#read only variable

NAME1="indulkar"
readonly NAME1

echo "$NAME1"

#unset stored variable value, cant reset readonly variable

NAME3="vinayak"
unset NAME3

echo $NAME3
