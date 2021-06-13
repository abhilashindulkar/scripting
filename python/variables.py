#assigning values to the multiple variables

x, y, z = 1, 2, 3
print (x,y,z)

# assignment of multiple variables to single value

a=b=c=100
print(a,b,c)

#unpack the collection

fruits=["apple","banana","mango"]
p,q,r=fruits

print(p,q,r)

# output the variables

name='Abhilash'

print ("welcome " + name)

x = "Python is "
y = "cool"
z =  x + y
print(z)


#global variables

var_1 = 'awesome'

def my_function():
    print ("python is " + var_1)

my_function()

var_2 ='good'

def my_func():
    var_2='fantastic'
    print("python is " + var_2)

my_func()

print ('python is ' + var_2)

def my_funct():
    global var_3
    var_3='beautiful'

my_funct()

print ('python is ' + var_3)