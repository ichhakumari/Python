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
