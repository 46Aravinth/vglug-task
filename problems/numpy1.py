import numpy as np 
a=np.array([1,2,3])
print(a)
b=a.copy()
print(b)
b[2]=5
print(b)
c=a.view()
print(c)
c[2]=6
print(c)
print(a)
print(c.base)
print(a.base)

a=np.array([1,2,3,4,5,6,7,8])
print(a)
b=a.reshape((1,4,2))
print(b)