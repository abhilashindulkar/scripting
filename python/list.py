ls=[10,"Abhilash",-2,4.5,True]
print(ls)
print(ls[4])
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