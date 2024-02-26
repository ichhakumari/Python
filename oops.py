# oops in python
class Phone:
  def make_call(self):
    print("making call")

  def play_game(self):
    print("playing games")

#creating instnces / object of class
p1=Phone()

#invokig methods
p1.make_call()

p1.play_game()

# adding parameters
class Mobile:
  def set_color(self,color):
    self.color=color

  def set_cost(self,cost):
    self.cost=cost

  def show_color(self):
    return self.color

  def show_cost(self):
    return self.cost

p2 = Mobile()

p2.set_color("black")
p2.set_cost(6000)

print(p2.show_color())
print(p2.show_cost())


#constructor
class Employee:
   def __init__(self,name,age,salary,gender):   #constructor
     self.name = name
     self.age = age
     self.salary = salary
     self.gender = gender

   def show_details(self):
    print("Name of employee is" ,self.name)
    print("Age of employee is" ,self.age)
    print("salary of employee is" ,self.salary)
    print("gender of employee is" ,self.gender)

e1= Employee('ram',32,50000,'male')

e1.show_details()

#Inheritance
#base class
class Vehicle:
    def __init__(self, mileage, cost):
        self.mileage = mileage
        self.cost = cost

    def show_details(self):
        print("mileage of vehicle is", self.mileage)
        print("cost of vehicle is", self.cost)

v1= Vehicle(300,500000)
v1.show_details()

#child class

class car(Vehicle):    #inherit vehicle class
  def show_car_details(self):
      print("i am car")

c1=car(250,4000)
c1.show_details()
c1.show_car_details()

#overridding
class bike(Vehicle):
  def __init__(self, mileage, cost, tyres, hp):
     super().__init__(mileage, cost)
     self.tyres = tyres
     self.hp = hp

  def show_bike_details(self):
      print("no of tyres in bike:", self.tyres)
      print("horse power of bike is:", self.hp)

b1 = bike(300, 50000, 2, 989)
b1.show_bike_details()

# types of inheritance  -> single, multiple, multi-level , hybride
#multiple -> 2parents

class Parent1():
  def assign_string_one(self,str1):
      self.str1= str1

  def show_str_one(self):
      return self.str1

class Parent2():
  def assign_string_two(self,str2):
      self.str2= str2

  def show_str_two(self):
      return self.str2

#child class
class Derived(Parent1, Parent2):
  def assign_string_three(self,str3):
      self.str3= str3

  def show_str_three(self):
      return self.str3

d1=Derived()

d1.assign_string_one("one")
d1.assign_string_two("two")
d1.assign_string_three("three")

print(d1.show_str_one())
print(d1.show_str_two())
print(d1.show_str_three())


#multilevel -> prent->child->grand child
class GrandChild(Derived):
  def assign_naam(self,naam):
    self.naam=naam

  def show_naam(self):
    return self.naam

g1= GrandChild()
g1.assign_naam("grand child")
g1.assign_string_one("parent one")
g1.assign_string_three("child one")

print(g1.show_naam())
print(g1.show_str_one())
print(g1.show_str_three())


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
