#!/bin/bash

echo $$ #PID of the shell

echo $0 #filename of the current script

echo $n #variables correspond to the arguments with which script was invoked

echo $# #no of the arg supplied to the script

echo $* #All the arguments are double quoted. If a script receives two arguments, $* is equivalent to $1 $2

echo $@ #All the arguments are individually double quoted

echo $? #The exit status of the last command executed

echo $! #the process no of last background command
