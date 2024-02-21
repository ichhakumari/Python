# variable
student="ram"
student

student="sita"
student   #output-> sita
#hence proved variable is  a temprary storage space

# data type
a=20
type(a)  #int
#boolean
b='true'
type(b)
#float
a=2.0
type(a)
 # complex ->real  & imeginary part
a=3+4j  
type(a)

#operator.....> Arithmetic operator
a=4
b=3
sum=a+b
diff=a-b
mul= a*b
div=a/b
mod=a%b
print(sum)
print(diff)
print(mul)
print(div)
print(mod)

#logical operator(&, |)
a=True
b=False
print(a&a)
print(a&b)
print(a|b)
print(a|a)

#relatonal operator (<,>,==,!=)
a=50
b=80
print(a>b)
print(a<b)
print(a==b)
print(a!=b)

# string
a='helllo'
b="ichha"
c='''multi
line
string'''
print(a)
print(b)
print(c)

# extracting individual char
string1= "python is a fun language"
print(string1[0])
print(string1[-1])

# string function
print(len(string1)) # length of string
print(string1.lower())
print(string1.upper())

#replaceing a substring
print(string1.replace('is','was'))

# number of occurance of substring
print(string1.count("a"))

# find -> finding the index of substring
print(string1.find('fun'))

# split -> splitting a string
fruits='i like apple,mangoes, banana'
print(fruits.split(','))

# data structure in python  -> tuple, list , dictionary ,set
# tuple -> ordered collection, store in(), immutable

tup1=(1,True,8.4,6-3)
print(tup1)
print(tup1[0])
print(tup1[-1])
print(tup1[1:3])
print(len(tup1))

#concate tuple
tup1=(2,3,4)
tup2=(5,6,7)

print(tup1+tup2)
print(tup2+tup1)

# repeating tuple element
tup1=('hi',30)
tup2=(4,5,6)
print(tup1*4)
print(tup1*4 +tup2)
print(min(tup2))
print(max(tup2))

#list -> mutable
l1=[1,2,'mango',4.5]
print(l1)
l1[1]=500
print(l1)
