import numpy as np
 # tao mang co 6 phan tu
a = np.array([0,1,2,3,4,5])
#hien thi mang a
print(a)
#hien thi so chieu cua a
print(a.ndim)
print(a.shape)
print(a[a>3])
a[a>3]=10
b=a.reshape((3,2))
print(b)
print(b[2][1])
b[2][0]=50
c=b*2
print(c)