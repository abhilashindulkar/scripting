s="hello world, this is abhilash"
print(len(s))

print(s[4])

print(s*3)

s1="""you are the 
    creator of your 
    destiny"""

print(len(s1))

print(s[0:7])

print(s[-3:-1])

print (s[0:9:2])

print (s[29::-1])  #reverse string

s3= "   i am learning python   "
print(s3)
print(s3.strip())   #strip--remove spaces

print(s3.find("py"))
print(s3.find("py",0,len(s3)))

print(s3.count('n'))
print(s3.replace("python","python with ML"))

print(s.upper())
print(s.lower())
print(s.title())