#!/usr/bin/python3

# Import module cbuilder
import cbuilder

### function to return a value from the calling program
# def square(x):
#     y = x * x
#     return y
#
# result = square(10)
# print(result)

# Function to create a character for 5e

print("Begining character creation ...")
### creates a new output text file using format shortname.txt
### in the same directory as nkosi5e.py

## Get Race, Class and Level Codes
print("D1 = Dwarf, E1 = Elf, H1 = Human, H2 = Halfling")
c_race = input("what is your character's race code: ")

print("F10 = Fighter, W6 = Wizard, B8 = Bard, C8 = Cleric, R8 = Rogue")
c_class = input("what is your character's class code: ")

c_level = int(input("what is your character's level: "))

#print("D1 = Dwarf, E1 = Elf, H1 = Human, H2 = Halfling")
#c_race = input("what is your character's race code: ")
#if (c_race in ['E1','D1','H2']):
#    if (c_race == 'E1'):
#        c_sub = input('Wood or High: ')
#        full_name = (c_name + "_" + c_sub + "-Elf")
#    elif (c_race == 'D1'):
#        c_sub = input('Mountain or Hill: ')
#        full_name = (c_name + "_" + c_sub + "-Dwarf")
#    else:
#        c_sub = input('Lightfoot or Stout: ')
#        full_name = (c_name + "_" + c_sub + "-Halfling")
#else:
#    c_sub = 'no_sub'
#    full_name = (c_name + "_Human")
#print("F10 = Fighter, W6 = Wizard, B8 = Bard, C8 = Cleric, R8 = Rogue")
#c_class = input("what is your character's class code: ")



# build the file name f_name that will be created in the same directory
#file_name = (c_class + "_" + full_name + ("_lv" + str(c_level)))



### need to open a file of format f_name.txt same directory
#File_object = open(r"File_Name","Access_Mode")
# Open function to open the file "file_name.txt", write mode
#file1 = open(((file_name)+".txt"),"w")
### prompt user to answer questions about profile and
# store its reference in the created file



# store response of player in file
# File_object.write(str1)

# file1.write('Character Name: ' + full_name +'\n')

if (c_class == 'F10'):
    print("c_class_name = 'Fighter'")
if (c_class == 'B8'):
    print("c_class_name = 'Bard'")
if (c_class == 'C8'):
    print("c_class_name = 'Cleric'")
if (c_class == 'R8'):
    print("c_class_name = 'Rogue'")
if (c_class == 'W6'):
    cbuilder.wizard(c_race, c_class, c_level)


# file1.write('Class: ' + c_class_name +"\n")
# file1.write('Level: ' + str(c_level) +"\n")
# file1.write('Hit Die: 1d'+(c_class[1:3])+"\n")
# file1.write('Background: ' + c_background +'\n')


# fightstyle = input("What style of fighter: ")
# file1.write('Fighting style: ' + fightstyle +"\n")

# print("\n Welcome to the Adventure...")
# print("    "+ c_name + " ~ Level " + str(c_level) +"\n")

