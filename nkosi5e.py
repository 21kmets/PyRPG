#### 5e Character Dev ####
# This is an attempt to work on my python by creating a script
# for building dnd characters
# It should use functions for modularity
# run from the bash terminal
# prompt the reader to make the relevant character design choices
# store those choices and potentially print them out to a file
# or deliver them to a rules engine governing rolls of engagement
#########

### build_char() function
# prompts the player to choose their
# character's base race, class and background
# Their choices will call other functions with specific prompts
# related their character's base traits.
# Inputs:
# c_name ~ a shortname for the character
# c_race ~ a race for the character
# c_class ~ a class for the character
# c_background ~ a background for the character
# Output:
# eventually a text file which doubles as the character sheet.
###

# Imports
import random

def build_char():
    print("\nD1 : Dwarf")
    print("E1 : Elf")
    print("H2 : Halfling")
    print("H1 : Human")
    c_race = (str(raw_input("Enter the code for your character's race: ")))
    if (c_race == "D1"):
        print("Nice to meet you " + c_race + "!")
    else:
        print("Sorry. That module has not been implemented yet!\n")
        build_char()
    print("B8 : Bard")
    print("C8 : Cleric")
    print("F10 : Fighter")
    print("R8 : Rogue")
    print("W6 : Wizard")
    c_class = (str(raw_input("Enter the code for your character's class: ")))
    if (c_class == "F10"):
        print("So you think your a Fighter, aye!")
    else:
        print("Sorry. That module has not been implemented yet!\n")
        build_char()
    print("Acolyte,Criminal,Entertainer,Sage or Soldier?")
    c_background = (str(raw_input("What's your character's background: ")))
    if (c_background == "Soldier"):
        print("So you were a " + c_background + "!")
    else:
        print("Sorry. That module has not been implemented yet!\n")
        build_char()
    c_name = (str(raw_input("What's your character's shortname: \n")))
    print("Welcome to the Adventure...")
    print("    "+c_name +": "+ c_race + "~" + c_class + c_background + "\n")

### calc_hp() function
# Function to calculate HP at different levels
# Inputs:
# c_class ~ character's class
# c_lvl ~ character's level
# c_con_mod ~ character's Constitution Modifier


# gets random dice roll
def roll_dice(a):
    return rand.int(1, a)

def calc_hp():
    print("\nF10 : Fighter")
    print("B8 : Bard")
    print("C8 : Cleric")
    print("R8 : Rogue")
    print("W6 : Wizard")
    c_class = (raw_input("What's your character's code: \n"))
    c_lvl = (int(input("What's your character's level: \n")))
    c_con_mod = (int(input("What's your character's constitution modifier: \n")))
    print("Enter 1 for standard stock calculation ")
    print("Enter 2 for standard Adventure's League calculation ")
    print("Enter 3 for House Rules calculation \n")
    hp_method = (int(input("Method of calculating HP without rolling: \n")))
    # Calculates Hit Points based on character and method
    if (hp_method == 1):
        print('Sorry, that method is unsupported.\n')
        print('Implementing ~ House Rules ...')
        # hp = (house_rules(c_class,c_lvl,c_con_mod))
    elif (hp_method == 2):
        print('Sorry, you are venturing into uncharted territory.\n')
        print('Implementing ~ House Rules ...')
        # hp = (house_rules(c_class,c_lvl,c_con_mod))
    elif (hp_method == 3):
        print('Thank you for observing Guest Rights!\n')
        print('Implementing ~ House Rules ...')
        # hp = (house_rules(c_class,c_lvl,c_con_mod))
    else:
        print('Implementing ~ House Rules ...')
    # Implementing House Rules regardless of choice. Maniacal Laughter ensues...
    # calculates HP based on House Rules ~ assumes player does not roll for Points
    hd = (int(c_class[1:3]))
    # calculates the size of the HD by slicing the c_class string eg. "F10" = 10
    if (c_lvl == 1):
        hp = (hd + c_con_mod)
        # adds the HD and Const modifier to calculate 1st lvl HP
        print("The character's Hit points are: " + str(hp))
    else:
        hp = ((hd + c_con_mod) + ((hd/2 + c_con_mod)*(c_lvl - 1)))
    # adds first lvl HP to remaining n-1 lvls to calculate n-lvl HP
        print("The character's Hit points are: " + str(hp))








    # Calculate type of HD (hit die) based on character's class

def calc_hd():
    print("F10 : Fighter")
    print("B8 : Bard")
    print("C8 : Cleric")
    print("R8 : Rogue")
    print("W6 : Wizard")
    c_class = (str(raw_input("Enter the code for your character's class: ")))
    if (c_class == 'F10'):
        hd = 10;  # Fighter uses 1d10 hit die
        print("1d10")
    elif (c_class == ['B8','C8','R8']):
        hd = 8;  # Bard, Cleric and Rogue all use 1d8 hit die
        print("1d8")
    elif (c_class == 'W6'):
        hd = 6;  # Wizard uses 1d6 hit die
        print("1d6")
    else:
        print("That's an invalid class for this campaign. ")


    # Calculate HP using chosen calculation

# Main Menu
def main_menu():
    print("1 : Build a Character")
    print("2 : Calculate Hit Die")
    print("3 : Calculate Hit Points")
    print("4 : Finished with Characters\n")
    choice = (int(input("Enter your choice as a number: ")))
    if (choice == 4):
        return
    elif (choice == 1):
        print("Building Character...")
        build_char();
    elif (choice == 2):
        print("Calculating Hit Die...")
        calc_hd();
    elif (choice == 3):
        print("Calculating Hit Points...")
        calc_hp();
    else:
        print("Invalid choice, please choose again...")
        main_menu();
main_menu();
