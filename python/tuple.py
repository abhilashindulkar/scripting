""" tuple
allows duplicates, immutable
indexing, slicing, repetition is possible
"""
t1=(1,2,3,4,1)
print(type(t1))
t2=1,
print(t2)

print(t1.count(1))
print(t1.index(2))
print(t1*2)

l1=[45,56,32,78,"XYZ"]
print(type(l1))
print(l1)

tp1=tuple(l1)
print(type(tp1))
print(tp1)

