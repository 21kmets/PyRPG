class AvSub:
    def __init__(self):
        self.c_name = (str(raw_input("What's your character's shortname: \n")))
        print("D1 = Dwarf, E1 = Elf, H1 = Human, H2 = Halfling")
        self.c_race = raw_input("what is your character's race code: ")
        if (self.c_race in ['E1','D1','H2']):
            if (self.c_race == 'E1'):
                self.c_sub = raw_input('Wood or High: ')
                self.full_name = (self.c_name + "_" + self.c_sub + "-Elf")
            elif (self.c_race == 'D1'):
                self.c_sub = raw_input('Mountain or Hill: ')
                self.full_name = (self.c_name + "_" + self.c_sub + "-Dwarf")
            else:
                self.c_sub = raw_input('Lightfoot or Stout: ')
                self.full_name = (self.c_name + "_" + self.c_sub + "-Halfling")
        else:
            self.c_sub = 'no_sub'
            self.full_name = (self.c_name + "_Human")
# define an ouput function ...
    def AvOutput(self):
        print("The Character's race is ..." + (self.c_race))
        print("The Character's sub race is ..." + (self.c_sub))
        print("The Character's Short Description is ..." + (self.full_name))

a1 = AvSub()
a1.AvOutput()
