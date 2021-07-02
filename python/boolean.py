#Boolean Values
print(10 > 9)
print(10 == 9)
print(10 < 9)

a=100
b=15

if a < b:
    print("a is less than b")
else:
    print("a is greater than b")

#Evaluate Values and Variables
print(bool("hello"))
print(bool(""))
print(bool(10))
print(bool(0))


#Functions can Return a Boolean
def my_func():
    return True

if my_func():
    print("returns true")
else:
    print("returns false")

str_1='100'
print(isinstance(str_1,str))