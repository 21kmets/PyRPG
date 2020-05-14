class Avatar:

  def __init__(self):

    self.name = (str(raw_input("What's your character's shortname: \n")))
    self.age = (input("What's your character's age: \n"))

  def myfunc(self):
    print("Hello my name is " + self.name)
    print("Hello my age is " + str(self.age))

p1 = Avatar()
p1.myfunc()

p2 = Avatar()
p2.myfunc()
