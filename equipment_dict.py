# Player's Handbook Equipment
import math

# List for Smith Tools ~ This python script tries to execute the system for
# using Smith's Tools created by Dump Stat Adventures find more content
# at DumpStatAdventures.com
#
# format of the list is a follows...
# item_name = [ 0,'Complexity','Weight','Cost','Days','DC','#checks','NP']
# where...
# [0]=['Y','N'] ~ is item craftable over a campfire? (have to be proficient)
# Complexity = ['Simple','Moderate','Complex'] ~ difficulty to make
# Weight = amount of iron materials in lbs required (float)
# Days = Number of days to craft a common item int(weight/4) rounded up
# DC = difficulty class for making a common item check (int)
# #checks = number of checks required to produce a common item (int)
# Cost = to produce the item paid up front in gold pieces (float)
# NP = no special properties & SP = Special properties see comments
#  (note: for Mastercraft, increase DC by +8 and cost by 3 times.)
#
# You need at least 6hours of crafting to complete a item, if you need
# more time ~ GM can use discretion to speed up the process
# but the number of crafting checks remain the same.

# Print('Simple Weapons')
dagger = ['Y', 'simple', 1.0, 1, 13, 1, 1.0, 'NP']
handaxe = ['Y', 'simple', 2.0, 1, 13, 1, 2.5, 'NP']
light_hammer = ['Y', 'simple', 2.0, 1, 13, 1, 1.0, 'NP']
mace = ['N', 'simple', 4.0, 1, 13, 1, 2.5, 'NP']
sickle = ['Y', 'moderate', 2.0, 1, 14, 1, 0.5, 'NP']
spear = ['Y', 'simple', 3.0, 1, 13, 1, 0.5, 'NP']
arrows = ['Y', 'simple', 0.0, 1, 13, 1, 0.5, 'SP']
darts = ['Y', 'simple', 0.25, 1, 13, 1, 0.02, 'SP']

# SP : arrowheads, darts & bolts ~ you can craft the number of
# arrowheads, darts and bolts in a single day equal to your Strength score.

# Print('Martial Weapons')
battleaxe = ['N', 'moderate', 4.0, 2, 14, 1, 5.0, 'NP']
flail = ['Y', 'complex', 2.0, 2, 15, 1, 5.0, 'NP']
glaive = ['N', 'moderate', 6.0, 3, 14, 1, 10.0, 'NP']
greataxe = ['N', 'moderate', 7.0, 4, 14, 1, 15.0, 'NP']
greatsword = ['N', 'moderate', 6.0, 3, 14, 1, 25.0, 'NP']
halberd = ['N', 'moderate', 6.0, 3, 14, 1, 10.0, 'NP']
longsword = ['Y', 'moderate', 3.0, 2, 14, 1, 7.5, 'NP']
maul = ['N', 'moderate', 10.0, 5, 14, 1, 5.0, 'NP']
morningstar = ['N', 'moderate', 4.0, 2, 14, 1, 7.5, 'NP']
pike = ['Y', 'moderate', 8.0, 2, 14, 1, 2.5, 'SP']
rapier = ['Y', 'moderate', 2.0, 1, 14, 1, 12.5, 'NP']
scimitar = ['Y', 'moderate', 3.0, 2, 14, 1, 12.5, 'NP']
shortsword = ['Y', 'moderate', 2.0, 1, 14, 1, 5.0, 'NP']
trident = ['N', 'moderate', 4.0, 2, 14, 1, 2.5, 'NP']
warpick = ['Y', 'moderate', 2.0, 1, 14, 1, 2.5, 'NP']
warhammer = ['Y', 'moderate', 2.0, 1, 14, 1, 7.5, 'NP']

# SP : Pike ~ has a long wooden shaft, may be harder to find than a
# normal wooden shaft. The metal spike of the pike will only take
# 2 days to craft

# Print('Armor')
studded_leather = ['Y', 'simple', 3.0, 1, 13, 1, 17.5, 'SP']
chain_shirt = ['Y', 'complex', 20.0, 20, 15, 3, 25.0, 'NP']
scale_mail = ['Y', 'moderate', 45.0, 23, 14, 4, 25.0, 'NP']
breastplate = ['N', 'simple', 20.0, 5, 13, 1, 200.0, 'NP']
half_plate = ['N', 'complex', 40.0, 40, 15, 6, 375.0, 'NP']
ring_mail = ['Y', 'complex', 40.0, 40, 15, 6, 15.0, 'NP']
chain_mail = ['Y', 'complex', 55.0, 55, 15, 8, 37.5, 'NP']
splint = ['Y', 'moderate', 60.0, 30, 14, 5, 100.0, 'NP']
plate = ['N', 'complex', 65.0, 65, 15, 10, 750.0, 'NP']
shield = ['Y', 'simple', 6.0, 2, 13, 1, 5.0, 'SP']


# SP : Studded Leather ~ you must have leather on hand before adding studs
# SP : Shield ~ depending on the material you are using, you won't be
# able to craft a shield with your Smith's Tools. Per GM discretion.

# Crafting Common & Scrap items : Costs half the gold of purchasing the item
# Mastercraft : Takes 25% more time than common items, costs 3x the Gold
# Mastercraft : adds either +1 to ATK Rolls or +1 to AC
# Scrap : Does not require any crafting checks, -1 to ATK Rolls or -1 to AC

# create a function to determine crafting costs, checks and quality.
# run it repeatedly until they say finished with crafting.

def smithing():
    crafting = 'Y'
    while (crafting == 'Y'):
        # ask them what they want to craft and determine then print out costs
        item_name = (str(raw_input("\n What would you like to craft? ")))
        item_quality = (str(raw_input("Scrap,Common or Mastercraft [S/C/M] : ")))
        # set mastercraft modifier for the attempted quality
        if (item_quality == 'M'):
            gold_mod = 3  # Mastercraft costs 3x more than common
            dc_mod = 8  # DC checks are increased by +8 for Mastercraft
            time_mod = 1.25  # takes 25% longer for Mastercraft
            print('\n Mastercraft quality: +1 to atk rolls or +1 to AC')
        elif (item_quality == 'S'):
            gold_mod = 1  # crafting costs half the purchase price for Scrap
            print('\n There are no DC checks for producing Scrap quality')
            print('Scrap quality: -1 to atk rolls or -1 to AC')
        else:
            gold_mod = 1  # crafting costs half the purchase price for Common

        if (item_name in ['arrows', 'bolts', 'darts', 'pike', 'studded_leather']):
            # check to see if item has SP : special properties
            if (item_name == 'studded_leather'):
                print("You must pay the cost of " + str(17.5 * gold_mod) + " gp and 3 lbs of iron,")
                print("You must also have leather on hand, before adding the studs.")
                print("it will take approximately 1 day to craft,")
                print(" and require 1 DC=" + str(13 + dc_mod) + " Strength Check")
            elif (item_name == 'pike'):
                # Pike
                print("\n You must pay the cost of " + str(2.5 * gold_mod) + " gp and 2 lbs of iron,")
                print("You must also have a 8-10 foot hardwood pole on hand.")
                print("it will take approximately " + str(int(math.ceil(2 * time_mod))) + "days to craft,")
                print(" and require 1 DC=" + str(13 + dc_mod) + " Strength Check")
            elif (item_name == 'darts'):
                # darts
                print("Each day you can craft the number of darts")
                print("equal to your Strength score, for 0.2 gp")

            else:
                # arrrows or bolts
                print("Each day you can craft the number of arrowheads or bolts")
                print("equal to your Strength score, for 0.5 gp")

        # Formulae for calculating NP items without special properties

        if (item_quality == 'M'):
            print('\n In order to make a Mastercraft ' + (item_name))
            print((item_name + '[4]'))
            print("\n You must pay the cost of " + str(2.5 * gold_mod) + " gp and 7 lbs of iron,")
            print("it will take approximately " + str(int(math.ceil(2 * time_mod))) + "days to craft,")
            print(" and require 1 DC=" + str(13 + dc_mod) + " Strength Check")
        elif (item_quality == 'S'):
            print('\n In order to make a Scrap ' + (item_name))
            print("\n You must pay the cost of " + str(2.5 * gold_mod) + " gp and 2 lbs of iron,")
            print("it will take approximately " + str(int(math.ceil(2 * time_mod))) + "days to craft,")
            print(" and require 1 DC=" + str(13 + dc_mod) + " Strength Check")
        else:
            print('\n Crafting a Common ' + (item_name) + ' costs half the purchase price')
            print("\n You must pay the cost of " + str(2.5 * gold_mod) + " gp and 2 lbs of iron,")
            print("it will take approximately " + str(int(math.ceil(2 * time_mod))) + "days to craft,")
            print(" and require 1 DC=" + str(13 + dc_mod) + " Strength Check")

        #        print("You must pay the cost of 17gp 5sp, have 3 lbs of iron,\n")
        #        print("and have leather, before adding the studs.\n")
        #        print("it will take approximately 1 day to craft,\n")
        #        print(" and require 1 DC=13 Strength Check\n")

        crafting = (str(raw_input("\n Would you like to continue crafting [Y/n] : ")))


smithing()

print("This is the EOF")
