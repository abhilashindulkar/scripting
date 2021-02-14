#!/bin/bash

a=40
b=30

if [ $a == $b ]
then
	echo "a is equal to b"
elif [ $a -lt $b ]
then
	echo "a is lesser than b"
else
	echo "a is greater than b"
fi

