#list
'''
List items are ordered, changeable, and allow duplicate values.
'''

ls=[10,"Abhilash",-2,4.5,True]
print(ls)
print(ls[1])
print(ls[-1])
print(ls[1:4])
print(ls*2)
print(len(ls))

ls.append(55)
ls.remove('Abhilash')
print(ls)

ls.reverse()
print(ls)

del(ls[1])
print(ls)

print(min(ls))
print(max(ls))

ls.insert(2,35)
print(ls)

ls.sort(reverse=True)
print(ls)

ls.clear()
print(ls)

#constructor
thislist=list(("apple", "banana", "cherry"))
print(thislist)

if "apple" in thislist:
    print("apple exists in this list")

thislist = ["apple", "banana", "cherry"]
tropical = ["mango", "pineapple", "papaya"]
thislist.extend(tropical)
print(thislist)

thislist = ["apple", "banana", "cherry"]
tropical = ("mango", "pineapple")
thislist.extend(tropical)
print(thislist)

thislist.pop(2)
thislist.remove("banana")
print(thislist)

thislist = ["apple", "banana", "cherry"]
for x in thislist:
  print(x)

thislist = ["apple", "banana", "cherry"]
for x in range(len(thislist)):
    print(thislist[x])

thislist = ["apple", "banana", "cherry"]
i=0
while i<len(thislist):
    print(thislist[i])
    i+=1

#loop comprehension
thislist = ["apple", "banana", "cherry", "book"]
[print(x) for x in thislist]

thislist.sort(reverse=True)
print(thislist)

thislist = ["apple", "banana", "cherry"]
mylist = thislist.copy()
print(mylist)
mylist=[120,34,45]
for x in mylist:
    thislist.append(x)
print(thislist)
thislist.count()