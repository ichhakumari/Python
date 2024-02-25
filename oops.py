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


