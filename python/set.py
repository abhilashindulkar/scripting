""" Set
no indexing,slicing,replication
doesn't allow duplicates"""


s1={1,5,45,23,5}
print(type(s1))
print(s1)

print(s1.update([22,67]))
print(s1)

l1=[20, 56,"abc",43]
st=set(l1)
print(type(st))
print(st)

f=frozenset(st)
#f.update([20])
