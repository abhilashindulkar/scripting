#!/bin/bash

value=`expr 2 + 2`	#addition
echo "total value: $value"

val1=10
val2=6

val3=`expr $val1 + $val2`	#addition
echo "total value: $val3"

val3=`expr $val1 - $val2`	#substraction
echo "total value: $val3"

val3=`expr $val1 / $val2`	#division
echo "total value: $val3"

val3=`expr $val1 \* $val2`	#multiplication
echo "total value: $val3"

val3=`expr $val1 % $val2`       #modulus
echo "total value: $val3"

val4=$val3
echo "value 4: $val4"


a=10
b=20

if [ $a == $b ]
then
	echo "a is equal to b"
else
	echo "a is not equal to b"
fi

if [ $a != $b ]
then
	echo "a is not equal to b"
else
	echo "a is equal to b"
fi

