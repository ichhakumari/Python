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

