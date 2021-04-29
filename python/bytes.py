l1=[10,42,45,13]
b1=bytes(l1)
print(type(b1))
print(b1)

b2=bytearray(l1)
print(type(b2))
b2[2]=27
print(b2)    #indexing, assignment are possible in bytearray