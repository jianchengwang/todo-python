from numpy import *

# create array
a = array([0, 1, 2, 3])
print(a)
print(type(a))
print(a.dtype)
print(a.itemsize)
print(a.shape)
print(a.ndim)

# init data
a.fill(-4.8)
print(a)

# slice
a = array([11,12,13,14,15])
print(a[0])
print(a[1:3])
a = array([[44, 45],
       [54, 55]])
print(a[:, 2])
print(a[2::2, ::2])