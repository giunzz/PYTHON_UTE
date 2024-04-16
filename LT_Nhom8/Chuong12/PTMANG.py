import numpy as np
a = np.linspace(1,12,12).reshape(4,3)
print(a)

print(a[3,1])
print(a[2,:])
print(a[:,1])
print(a[1:-1,1:])

a[:,1] = 0
print(a)

a = np.linspace(0.,0.5,6)
print(a)
ia = [1,4,5]
print(a[ia])

ia = np.array(((1,2), (3,4)))
print(a[ia])

a = np.linspace(1,12,12).reshape(4,3)
print(a)
ia = np.array(((1,0), (2,1)))
ja = np.array(((0,1), (2,1)))
print(a[ia,ja])
a = np.array([-2,-1,0,1,2])
ia = np.array([False,True,False,True,True])
print(a[ia])
print(a)
ib = a < 0
print(ib)
a[ib] = 0
print(a)
a = np.array([-2,-1,0,1,2])
a[a<0] = 0
print(a)
a = np.linspace(1,4,4).reshape(2,2)
print(a)
a.shape()
b = a[:,np.newaxis, : ]
print(b)
print(b.shape())