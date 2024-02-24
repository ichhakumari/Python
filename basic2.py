#Conditions
a=300
b=300

if a > b:
    print("a is greater than b")
elif a == b:
    print("a is equal to b")
else:
    
    print("b is greater")

i = 1
while i < 6:
  print(i)
  i += 1
else:
  print("i is no longer less than 6")

fruits = ["apple", "banana", "cherry"]
for x in fruits:
   print(x)

for x in "banana":
  print(x)

fruits = ["apple", "banana", "cherry"]
for x in fruits:
  print(x)
  if x == "banana":
    break


#function -> block of code which perform specfic task
def hello():
  print("hello python")

hello()

def odd_even(x):
  if x%2==0:
    print(x, "is even")
  else:
    print(x,"is odd")

odd_even(9)

#annourmous function - lambda function
g=lambda x: x*x*x

g(5)

# lambda with filter
#filter odd numbers
l1=[34,21,6,54,7,9,53]

final_list=list(filter(lambda x: (x%2!=0),l1))

final_list


#lambda with map   -> multiply all element with 2
l1=[1,2,3,4,5,6]
final_l1=list(map(lambda x: x*2,l1))

final_l1

#lambda with reduce function -> use to call a final sum or value
from functools import reduce
sum=reduce(lambda x,y: x+y,l1)

sum
