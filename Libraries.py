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

#extracting a single element
s1=pd.Series([1,2,3,4,5])
print(s1[3])

#extracting element fron back
print(s1[-3:])

#extracting series of element
print(s1[:2])

#adding scalar vallue on series elemt
print(s1 + 2)

#adding two series
s2=pd.Series([11,22,33,44,10,20,30])
print(s1+s2)

#other operations
print(s1-1)
print(s1/2)


#2.Data frame(multidimention labelled data -row nd column)
import pandas as pd
pd.DataFrame({"Name":['ram','sita','lakshman'],"marks":[80,87,89]})


# HOW TO WORK ON DATASETS.................................

# 1. IMPORT DATA SET
from google.colab import files


uploaded = files.upload()

import pandas as pd
import io
#store csv file in df variable..
df = pd.read_csv(io.BytesIO(uploaded['titanic_train.csv']))
print(df)


#for printing first 5 data
df.head()

# for last 5 record
df.tail()

# to see total no of row and column
df.shape

#to extract special column or row details...for ex: from row5 to11 and 3-5 column
#use iloc -work with index value
df.iloc[5:11,3:6]

# use loc - work with names of rows and columns
df.loc[0:3,("Name","Age")]

#drop row (axis=0) column(axis=1)
df.head()

df.drop('Pclass',axis=1)

#drop rows
df1=df.drop([1,3,5],axis=0)
df1

df1.head(10)


#pandas functions
df.mean()

df.median()

df.min()

df.max()

# half method

def half(s):
  return s*0.5

print(df[['Age','Fare']].apply(half))

#value count
df['Sex'].value_counts()

#sort_values
df.sort_values(by='Age')


#Mathplotlib libraries  - used for data visualization

#line plot
import numpy as np
from matplotlib import pyplot as plt

x=np.arange(1,11)
print(x)
y=x*2
print(y)

plt.plot(x,y)
plt.show()

#add title and labels in graph
plt.plot(x,y)
plt.title("Line plot")
plt.xlabel("x-label")
plt.ylabel("y-label")
plt.show()


#change line style..ex: color,style
plt.plot(x,y,color='r',linestyle=':',linewidth=5)
plt.show()


#two lines graph
x=np.arange(1,11)
y1=2*x
y2=3*x

plt.plot(x,y1,color='g',linestyle=':',linewidth='3')
plt.plot(x,y2,color='r',linestyle='-',linewidth='2')

plt.title("line plot")
plt.xlabel("x-axis")
plt.ylabel("y-axis")
plt.grid(True)
plt.show()

# adidng subplots
x=np.arange(1,11)
y1=2*x
y2=3*x

plt.subplot(1,2,1)
plt.plot(x,y1,color='g',linestyle=':',linewidth='3')
plt.title("line plot1")
plt.xlabel("x-axis")
plt.ylabel("y-axis")
plt.grid(True)


plt.subplot(1,2,2)
plt.plot(x,y2,color='r',linestyle='-',linewidth='2')

plt.title("line plot2")
plt.xlabel("x-axis")
plt.ylabel("y-axis")
plt.grid(True)
plt.show()



x=np.arange(1,11)
y1=2*x
y2=3*x

plt.subplot(2,1,1) #(2rows, 1column index)
plt.plot(x,y1,color='g',linestyle=':',linewidth='3')
plt.title("line plot1")
plt.xlabel("x-axis")
plt.ylabel("y-axis")
plt.grid(True)

plt.subplot(2,1,2)
plt.plot(x,y2,color='r',linestyle='-',linewidth='2')

plt.title("line plot2")
plt.xlabel("x-axis")
plt.ylabel("y-axis")
plt.grid(True)
plt.show()





#Bar plot
student={"bunty":8,"megha":100,"jay":59}
names=list(student.keys())
values=list(student.values())


plt.title("Bar plot")
plt.xlabel("students")
plt.ylabel("marks of student")
plt.grid(True)

plt.bar(names,values)
plt.show()


#Bar plot
student={"bunty":8,"megha":100,"jay":59}
names=list(student.keys())
values=list(student.values())


plt.title("Bar plot")
plt.xlabel("students")
plt.ylabel("marks of student")
plt.grid(True)

plt.bar(names,values)
plt.show()
