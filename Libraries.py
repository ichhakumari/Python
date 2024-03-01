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


# random number generation -> random.randint(start,end,no of random number)
import numpy as np
r1=np.random.randint(1,100,3)
print(r1)

r2=np.random.randint(1,100,10)
print(r2)

# change shape of array
import numpy as np
a1=np.array([[11,12,3,2,],[5,6,77,44]]) #(2,4)
print(a1)

a1.shape=(4,2)
print(a1)

a1.shape=(8,1)
print(a1)


#Joining numpy array
#1.vstack()-> vertically,hstack()-> horizontally 3.column_stack
import numpy as np
n1=np.array([22,33,44,55])
n2=np.array([21,32,33,54])
print(np.vstack((n1,n2)))   #vstack

#hstack
print(np.hstack((n1,n2)))

#column_stack
print(np.column_stack((n1,n2)))


#numpy Intersection(same) & diffrence
import numpy as np
n1=np.array([10,20,30,40])
n2=np.array([30,40,50,60,70])

print(np.intersect1d(n1,n2))

print(np.setdiff1d(n1,n2))
print(np.setdiff1d(n2,n1))


#mean , median,standard division
import numpy as np
n1=np.array([10,20,30,40])

print(np.mean(n1))
print(np.median(n1))
print(np.std(n1))

#mathemtics
#sum of whole array
import numpy as np
n1=np.array([10,20])
n2=np.array([30,40])
print(np.sum([n1,n2]))

#only column->axis=0
print(np.sum([n1,n2],axis=0))

#only row->axis=1
print(np.sum([n1,n2],axis=1))

#basic addition
n1=n1+1
print(n1)

n2=n2-2
print(n2)

n1=n1*2
print(n1)

n1=n1/2
print(n1)


#pandas(panel data) -> data manipulation
#ds in pandas -> 1. series(one dimenstion labeled data) 2.Data frame(multidimention labelled data -row nd column)

import pandas as pd
s1=pd.Series([1,2,3,4,5])
s2=pd.Series([1,2,3,4,5],index=['a','b','c','d','e'])
print(s1)
print(s2)
print(type(s1))


#create serial object from a  dictionary
import pandas as pd
pd.Series({'a':10,'b':20,'c':30})
#change index
pd.Series({'a':10,'b':20,'c':30},index=['b','c','a','d'])

