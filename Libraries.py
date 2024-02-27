#Numpy-> Numerical Python ->computation
# use array and multi dimenstion array
import numpy as np
n1=np.array([10,20,30,44])  # single array
print(n1)

#multi dimentional array
n2=np.array([[11,22,33,44],[43,53,63,73],[66,77,88,99]])
print(n2)

print(type(n1))
print(type(n2))

#initializing numpy Zeros
import numpy as np
a1=np.zeros((1,2))  #(row,column)
print(a1)

a2=np.zeros((5,5))  #(row,column)
print(a2)

# same number in array -> full method
import numpy as np
f1=np.full((3,4), 20) #(row,col),number
print(f1)

#range
n1=np.arange(10,100)  #(start,end)
print(n1)

n2=np.arange(10,50,5)    #(start,end, gap)
print(n2)


