#!/usr/bin/python3

# Import module math
import math
  
def print_func( par ):
   print ("Hello : ", par)
   return

def wizard(c_race, c_class, c_level):
   # define a wizard of level c_level
   print ("Creating Wizard, level : " + str(c_level))
   c_class_name = 'Wizard'


   # Enter these randomly generated values, or roll to determine your character's starting abilities
   print (' 6 values determined by rolling 4d6 and taking the best 3d6 each time'+'\n')
   # function to randomly roll 6 starting abilities
   strength = (input("Enter your character's Strength (STR): "))
   dexterity = (input("Enter your character's Dexterity (DEX) : "))
   constitution = (input("Enter your character's Constitution (CON) : "))
   intelligence = (input("Enter your character's Intelligence (INT) : "))
   wisdom = (input("Enter your character's Wisdom (WIS) : "))
   charisma = (input("Enter your character's Charisma (CHR) : "))

   # Begin fleshing out the character's background
   print("Acolyte, Criminal, Entertainer, Outlander, Sage or Soldier?")
   c_background = input("what is your character's background: ")

   # Shortname for the character in order to start building the character's file
   c_name = (str(input("What's your character's shortname: \n")))


   # build the file name f_name that will be created in the same directory
   if (c_race == 'E1'):
      c_sub = input('Wood or High: ')
      full_name = (c_name + "_" + c_sub + "-Elf")
      dexterity = dexterity + 2
      # Elf Weapon Training ~ proficient at long and short swords, and long and short bows.
      # base walking speed is 30ft
      # Darkvision ~ 60ft dim is light, and 60ft dark is dim, only shades of grey
      # Keen senses ~ proficiency in the Perception skill
      # Fey Ancestry ~ advantage on saving throws against being charmed, and magic can't put you to sleep.
      # Trance ~ 4 hours of trance, gains the same rest a human would from 8 hours of sleep
      # Languages ~ Common, and Elvish
      if (c_sub == 'Wood'):
         wisdom = wisdom + 1
         # fleet of foot ~ base walking speed becomes 35ft
         # Mask of the Wild ~ can attempt to hide even when you are only lightly obscured by natural phenomena.
      else:    # it's a muckty muck HIGH Elf
         intelligence = intelligence + 1
         # Bonus Wizard Cantrip cast with INT
         # Extra Language ~ speak, read and write one extra language
   if (c_race == 'D1'):
      c_sub = input('Mountain or Hill: ')
      full_name = (c_name + "_" + c_sub + "-Dwarf")
      if (c_sub == 'Mountain'):
          print('Mountain dwarf')
      else:
          print('Hill Dwarf')

   if (c_race == 'H2'):
      c_sub = input('Lightfoot or Stout: ')
      full_name = (c_name + "_" + c_sub + "-Halfling")
   if (c_race == 'H1'):
      c_sub = 'no_sub'
      full_name = (c_name + "_Human")
      # base walking speed is 30ft
      # languages ~ Common, and one other language
      h1_trait = (input('Are you using the feat optional human trait? [Y/n] : '))
      if (h1_trait == 'Y'):
         c_feat = (str(input("What's your character's feat: \n")))
         c_bonus_skill_proficiency = (str(input("which skill would you like to be proficient in? :")))
         # get +1 in two abilities of your choice.
         print('congrats your proficient in ...' + c_bonus_skill_proficiency)
      else:
         c_feat = 'None'
         strength = strength +1
         dexterity = dexterity +1
         constitution = constitution +1
         intelligence = intelligence +1
         wisdom = wisdom +1
         charisma = charisma +1
         print('Alles is een punt better : +1 All a round' + '\n')

   file_name = (c_class + "_" + full_name + ("_lv" + str(c_level)))

   ### need to open a file of format f_name.txt same directory
   # File_object = open(r"File_Name","Access_Mode")
   # Open function to open the file "file_name.txt", write mode
   file1 = open(((file_name) + ".txt"), "w")
   ### prompt user to answer questions about profile and
   # store its reference in the created file

   # store response of player in file
   # File_object.write(str1)

   file1.write('Character Name: ' + full_name + '\n')

   file1.write('Class: ' + c_class_name + "\n")
   file1.write('Level: ' + str(c_level) + "\n")
   file1.write('Hit Die: 1d' + (c_class[1:3]) + "\n")
   file1.write('Background: ' + c_background + '\n')
   file1.write('Optional Feat: ' + c_feat + '\n')
   file1.write('\n')
   file1.write('Proficiencies: ' + '\n')
   file1.write('-------------- ' + '\n')
   file1.write('Armor: None ' + '\n')
   file1.write('Weapons: Daggers, darts, slings, quarterstaffs, light crossbows ' + '\n')
   file1.write('Tools: None ' + '\n')
   file1.write('Saving Throws: Intelligence, Wisdom ' + '\n')
   skills2 = (str(input('pick 2 skills from : Arcana, History, Insight, Investigation, Medicine, and Religion:' +'\n')))
   file1.write('skills: '+ skills2 +'\n')
   file1.write('skills: ' + c_bonus_skill_proficiency)
   equip1 = (str(input('pick either a dagger or a quarterstaff:' + '\n')))
   equip2 = (str(input('pick either a Component pouch or a arcane focus:' + '\n')))
   equip3 = (str(input('pick either a scholar pack or a explorer pack:' + '\n')))
   file1.write('\n')
   file1.write('Equipment: ' + '\n')
   file1.write('---------- ' + '\n')
   file1.write(equip1 + '\n')
   file1.write(equip2 + '\n')
   file1.write(equip3 + '\n')

   # Number of spells you can prepare a day = INT + Wizard Level
   # Spells must be of a level that you have slots for.

   # Spell save DC = 8 + Proficiency bonus + INT

   # Spell attack modifier = Proficiency bonus + INT modifier

   if (c_feat == 'Spell Sniper'):
      print('You get a bonus cantrip to be picked from wiz, druid, ...'+'\n')
      bonus_cantrip = (str(input('Bonus Cantrip: ' + '\n')))
      file1.write('Spell Sniper ~ Bonus Cantrip: ' + bonus_cantrip + '\n')
   # section to calculate which questions to ask per level



   if (c_level >= 1):
      print('Level 1 : Proficiency +2, Spell Casting, Arcane Recovery, Spells ~ 3,2'+'\n')
      file1.write('\n')
      file1.write('Level 1 : Proficiency +2'+'\n')
      file1.write('Spells ~ 3,2'+'\n')
      file1.write('#Spell Casting# ~ INT ' + '\n')
      file1.write('Spell save DC = 8 + Proficiency bonus + INT : ' + '\n')
      file1.write('Spell attack modifier = Proficiency bonus + INT : ' + '\n')
      file1.write('#Ritual Casting# ~ You do not need to prepare to cast a Wizard Ritual spell that is in your spellbook. ' + '\n')
      file1.write('Ritual Casting ~  ' + '\n')
      file1.write('#Spell Casting Focus# ~ either component pouch or arcane focus ' + '\n')
      file1.write('#Learn new spells# ~ by adding 2 Wizard spells for free per level that you have slots ' + '\n')
      file1.write('Find other new spells on your adventures, and add them to your book ' + '\n')
      file1.write('If you can prepare it, and take the time to decipher and copy it ' + '\n')
      file1.write('For each level of the spell costs 2hrs & 50gp. The cost represents material components you expend, ' + '\n')
      file1.write('in your attempts to master the spell. Copying your own spells cost 1hr & 10gp' + '\n')
      file1.write('#Arcane Recovery# ~ recover spell slots, regain magical energy by studying your spellbook.' + '\n')
      file1.write('Once per day after a short rest is completed ~ recover roundup(wizardlevel/2) spellslot levels ' + '\n')

      file1.write('1 Cantrip : ' + '\n')
      file1.write('2 Cantrip : ' + '\n')
      file1.write('3 Cantrip : ' + '\n')
      file1.write(' ' + '\n')
      file1.write('Spell 1 : ' + '\n')
      file1.write('Spell 2 : ' + '\n')
      file1.write('Spell 3 : ' + '\n')
      file1.write('Spell 4 : ' + '\n')
      file1.write('Spell 5 : ' + '\n')
      file1.write('Spell 6 : ' + '\n')

   if (c_level >= 2):
      print('Level 2 : Arcane Tradition, Spells ~ 3,3'+'\n')
      print('Choose a Arcane Tradition : Abjuration, Conjuration, Divination, Enchantment, Evocation, Illusion, Necromancy or Transmutation.')
      arc_trad = (str(input('Arcane Tradition : ' + '\n')))
      file1.write('\n')
      file1.write('Level 2 : ' + '\n')
      file1.write('Spell slots ~ 3,3' + '\n')
      file1.write('#Arcane Tradition# ~ ' + arc_trad + '\n')

      file1.write('You can learn 2 new spells per level' + '\n')
      file1.write('Spell 7 : ' + '\n')
      file1.write('Spell 8 : ' + '\n')

   if (c_level >= 3):
      print('Level 3 : +2 ---, Spells ~ 3,4,2'+'\n')
      file1.write('\n')
      file1.write('Level 3 : '+'\n')
      file1.write(' ---, Spell slots ~ 3,4,2' + '\n')
      file1.write('Spell 9 : ' + '\n')
      file1.write('Spell 10 : ' + '\n')

   if (c_level >= 4):
      print('Level 4 : +2 Ability Score+2, Spells ~ 4,4,3'+'\n')
      file1.write('\n')
      file1.write('Level 4 : '+'\n')
      file1.write('Ability Score, Spell slots ~ 4,4,3' + '\n')
      scores = (input('Would you like to increase 2 Ability Scores or 1 Ability Score, enter 2 or 1 : '))
      if (scores == 2):
         score1 = (input('Enter the number: 1Strength, 2Dexterity, 3Constitution, 4Intelligence, 5Wisdom, 6Charisma : '))
         score2 = (input('Enter the number: 1Strength, 2Dexterity, 3Constitution, 4Intelligence, 5Wisdom, 6Charisma :'))
         if (score1 or score2 == 1): #Strength +1
            strength = strength + 1
         if (score1 or score2 == 2):  #Dexterity +1
            dexterity = dexterity + 1
         if (score1 or score2 == 3):   #Constitution +1
            constitution = constitution + 1
         if (score1 or score2 == 4):    #Intelligence +1
            intelligence = intelligence + 1
         if (score1 or score2 == 5):    #Wisdom +1
            wisdom = wisdom + 1
         if (score1 or score2 == 6):    #Charisma +1
            charisma = charisma + 1
      else:
         print('Increase an Ability by 2pts: 1Strength, 2Dexterity, 3Constitution, 4Intelligence, 5Wisdom, 6Charisma :')
         score1 = (input('Pick the number you would like to increase : '))
         file1.write(score1 + ' + 2' + '\n')
         if (score1 == 1):
            strength = strength + 2
         if (score1 == 2):
            dexterity = dexterity + 2
         if (score1 == 3):
            constitution = constitution + 2
         if (score1 == 4):
            intelligence = intelligence + 2
         if (score1 == 5):
            wisdom = wisdom + 2
         if (score1 == 6):
            charisma = charisma + 2
      file1.write('Spell 11 : ' + '\n')
      file1.write('Spell 12 : ' + '\n')

   if (c_level >= 5):
      print('Level 5 : +3 ---, Spells ~ 4,4,3,2'+'\n')
      file1.write('\n')
      file1.write('Level 5 : Proficiency +3'+'\n')
      file1.write('---, Spell slots ~ 4,4,3,2' + '\n')
      file1.write('Spell 13 : ' + '\n')
      file1.write('Spell 14 : ' + '\n')

   if (c_level >= 6):
      print('Level 6 : +3 Arcane Tradition Feature, Spells ~ 4,4,3,3'+'\n')
      file1.write('\n')
      file1.write('Level 6 : '+'\n')
      file1.write('Arcane Tradition Feature, Spell slots ~ 4,4,3,3' + '\n')
      file1.write('Spell 15 : ' + '\n')
      file1.write('Spell 16 : ' + '\n')

   if (c_level >= 7):
      print('Level 7 : +3 ---, Spells ~ 4,4,3,3,1'+'\n')
      file1.write('\n')
      file1.write('Level 7 : '+'\n')
      file1.write('---, Spell slots ~ 4,4,3,3,1' + '\n')
      file1.write('Spell 17 : ' + '\n')
      file1.write('Spell 18 : ' + '\n')

   if (c_level >= 8):
      print('Level 8 : +3 Ability Score+2, Spells ~ 4,4,3,3,2) '+'\n')
      file1.write('\n')
      file1.write('Level 8 : '+'\n')
      file1.write('Ability Score, Spell slots ~ 4,4,3,3,2) ' + '\n')

      scores = (input('Would you like to increase 2 Ability Scores or 1 Ability Score, enter 2 or 1 : '))
      if (scores == 2):
         score1 = (
            input('Enter the number: 1Strength, 2Dexterity, 3Constitution, 4Intelligence, 5Wisdom, 6Charisma : '))
         score2 = (input('Enter the number: 1Strength, 2Dexterity, 3Constitution, 4Intelligence, 5Wisdom, 6Charisma :'))
         if (score1 or score2 == 1):  # Strength +1
            strength = strength + 1
         if (score1 or score2 == 2):  # Dexterity +1
            dexterity = dexterity + 1
         if (score1 or score2 == 3):  # Constitution +1
            constitution = constitution + 1
         if (score1 or score2 == 4):  # Intelligence +1
            intelligence = intelligence + 1
         if (score1 or score2 == 5):  # Wisdom +1
            wisdom = wisdom + 1
         if (score1 or score2 == 6):  # Charisma +1
            charisma = charisma + 1
      else:
         print('Increase an Ability by 2pts: 1Strength, 2Dexterity, 3Constitution, 4Intelligence, 5Wisdom, 6Charisma :')
         score1 = (input('Pick the number you would like to increase : '))
         file1.write(score1 + ' + 2' + '\n')
         if (score1 == 1):
            strength = strength + 2
         if (score1 == 2):
            dexterity = dexterity + 2
         if (score1 == 3):
            constitution = constitution + 2
         if (score1 == 4):
            intelligence = intelligence + 2
         if (score1 == 5):
            wisdom = wisdom + 2
         if (score1 == 6):
            charisma = charisma + 2
      file1.write('Spell 19 : ' + '\n')
      file1.write('Spell 20 : ' + '\n')

   if (c_level >= 9):
      print('Level 9: +4 ---, Spells ~ 4,4,3,3,3,1'+'\n')
      file1.write('\n')
      file1.write('Level 9: Proficiency +4'+'\n')
      file1.write('---, Spell slots ~ 4,4,3,3,3,1' + '\n')
      file1.write('Spell 21 : ' + '\n')
      file1.write('Spell 22 : ' + '\n')

   if (c_level >= 10):
      print('Level 10 : +4 Arcane Tradition Feature, Spells ~ 5,4,3,3,3,2 '+'\n')
      file1.write('\n')
      file1.write('Level 10 : '+'\n')
      file1.write('Arcane Tradition Feature, Spell slots ~ 5,4,3,3,3,2 ' + '\n')
      file1.write('Spell 23 : ' + '\n')
      file1.write('Spell 24 : ' + '\n')

   if (c_level >= 11):
      print('Level 11 : +4 ---, Spells ~ 5,4,3,3,3,2,1'+'\n')
      file1.write('\n')
      file1.write('Level 11 : '+'\n')
      file1.write('---, Spell slots ~ 5,4,3,3,3,2,1' + '\n')
      file1.write('Spell 25 : ' + '\n')
      file1.write('Spell 26 : ' + '\n')

   if (c_level >= 12):
      print('Level 12 : +4 Ability Score+2, Spells ~ 5,4,3,3,3,2,1 '+'\n')
      file1.write('\n')
      file1.write('Level 12 : '+'\n')
      file1.write('Ability Score, Spell slots ~ 5,4,3,3,3,2,1 ' + '\n')
      scores = (input('Would you like to increase 2 Ability Scores or 1 Ability Score, enter 2 or 1 : '))
      if (scores == 2):
         score1 = (
            input('Enter the number: 1Strength, 2Dexterity, 3Constitution, 4Intelligence, 5Wisdom, 6Charisma : '))
         score2 = (input('Enter the number: 1Strength, 2Dexterity, 3Constitution, 4Intelligence, 5Wisdom, 6Charisma :'))
         if (score1 or score2 == 1):  # Strength +1
            strength = strength + 1
         if (score1 or score2 == 2):  # Dexterity +1
            dexterity = dexterity + 1
         if (score1 or score2 == 3):  # Constitution +1
            constitution = constitution + 1
         if (score1 or score2 == 4):  # Intelligence +1
            intelligence = intelligence + 1
         if (score1 or score2 == 5):  # Wisdom +1
            wisdom = wisdom + 1
         if (score1 or score2 == 6):  # Charisma +1
            charisma = charisma + 1
      else:
         print('Increase an Ability by 2pts: 1Strength, 2Dexterity, 3Constitution, 4Intelligence, 5Wisdom, 6Charisma :')
         score1 = (input('Pick the number you would like to increase : '))
         file1.write(score1 + ' + 2' + '\n')
         if (score1 == 1):
            strength = strength + 2
         if (score1 == 2):
            dexterity = dexterity + 2
         if (score1 == 3):
            constitution = constitution + 2
         if (score1 == 4):
            intelligence = intelligence + 2
         if (score1 == 5):
            wisdom = wisdom + 2
         if (score1 == 6):
            charisma = charisma + 2
      file1.write('Spell 27 : ' + '\n')
      file1.write('Spell 28 : ' + '\n')

   if (c_level >= 13):
      print('Level 13 : +5 ---, Spells ~ 5,4,3,3,3,2,1,1'+'\n')
      file1.write('\n')
      file1.write('Level 13 : Proficiency +5'+'\n')
      file1.write('---, Spell slots ~ 5,4,3,3,3,2,1,1' + '\n')
      file1.write('Spell 29 : ' + '\n')
      file1.write('Spell 30 : ' + '\n')

   if (c_level >= 14):
      print('Level 14 : +5 Arcane Tradition Feature, Spells ~ 5,4,3,3,3,2,1,1 '+'\n')
      file1.write('\n')
      file1.write('Level 14 : '+'\n')
      file1.write('Arcane Tradition Feature, Spell slots ~ 5,4,3,3,3,2,1,1 ' + '\n')
      file1.write('Spell 31 : ' + '\n')
      file1.write('Spell 32 : ' + '\n')

   if (c_level >= 15):
      print('Level 15 : +5 ---, Spells ~ 5,4,3,3,3,2,1,1,1'+'\n')
      file1.write('\n')
      file1.write('Level 15 : '+'\n')
      file1.write('---, Spell slots ~ 5,4,3,3,3,2,1,1,1' + '\n')
      file1.write('Spell 33 : ' + '\n')
      file1.write('Spell 34 : ' + '\n')

   if (c_level >= 16):
      print('Level 16 : +5 Ability Score+2, Spells ~ 5,4,3,3,3,2,1,1,1 '+'\n')
      file1.write('\n')
      file1.write('Level 16 : '+'\n')
      file1.write('Ability Score, Spell slots ~ 5,4,3,3,3,2,1,1,1 ' + '\n')

      scores = (input('Would you like to increase 2 Ability Scores or 1 Ability Score, enter 2 or 1 : '))
      if (scores == 2):
         score1 = (
            input('Enter the number: 1Strength, 2Dexterity, 3Constitution, 4Intelligence, 5Wisdom, 6Charisma : '))
         score2 = (input('Enter the number: 1Strength, 2Dexterity, 3Constitution, 4Intelligence, 5Wisdom, 6Charisma :'))
         if (score1 or score2 == 1):  # Strength +1
            strength = strength + 1
         if (score1 or score2 == 2):  # Dexterity +1
            dexterity = dexterity + 1
         if (score1 or score2 == 3):  # Constitution +1
            constitution = constitution + 1
         if (score1 or score2 == 4):  # Intelligence +1
            intelligence = intelligence + 1
         if (score1 or score2 == 5):  # Wisdom +1
            wisdom = wisdom + 1
         if (score1 or score2 == 6):  # Charisma +1
            charisma = charisma + 1
      else:
         print('Increase an Ability by 2pts: 1Strength, 2Dexterity, 3Constitution, 4Intelligence, 5Wisdom, 6Charisma :')
         score1 = (input('Pick the number you would like to increase : '))
         file1.write(score1 + ' + 2' + '\n')
         if (score1 == 1):
            strength = strength + 2
         if (score1 == 2):
            dexterity = dexterity + 2
         if (score1 == 3):
            constitution = constitution + 2
         if (score1 == 4):
            intelligence = intelligence + 2
         if (score1 == 5):
            wisdom = wisdom + 2
         if (score1 == 6):
            charisma = charisma + 2
      file1.write('Spell 35 : ' + '\n')
      file1.write('Spell 36 : ' + '\n')

   if (c_level >= 17):
      print('Level 17 : +6 ---, Spells ~ 5,4,3,3,3,2,1,1,1,1'+'\n')
      file1.write('\n')
      file1.write('Level 17 : Proficiency +6'+'\n')
      file1.write('---, Spell slots ~ 5,4,3,3,3,2,1,1,1,1' + '\n')
      file1.write('Spell 37 : ' + '\n')
      file1.write('Spell 38 : ' + '\n')

   if (c_level >= 18):
      print('Level 18 : +6 ,Spell Mastery, Spells ~ 5,4,3,3,3,3,1,1,1,1'+'\n')
      file1.write('\n')
      file1.write('Level 18 : '+'\n')
      file1.write('Spell Mastery, Spell slots ~ 5,4,3,3,3,3,1,1,1,1' + '\n')
      file1.write('Spell 39 : ' + '\n')
      file1.write('Spell 40 : ' + '\n')

   if (c_level >= 19):
      print('Level 19 : +6 Ability Score+2, Spells ~ 5,4,3,3,3,3,2,1,1,1 '+'\n')
      file1.write('\n')
      file1.write('Level 19 : '+'\n')
      file1.write('Ability Score, Spell slots ~ 5,4,3,3,3,3,2,1,1,1 ' + '\n')

      scores = (input('Would you like to increase 2 Ability Scores or 1 Ability Score, enter 2 or 1 : '))
      if (scores == 2):
         score1 = (
            input('Enter the number: 1Strength, 2Dexterity, 3Constitution, 4Intelligence, 5Wisdom, 6Charisma : '))
         score2 = (input('Enter the number: 1Strength, 2Dexterity, 3Constitution, 4Intelligence, 5Wisdom, 6Charisma :'))
         if (score1 or score2 == 1):  # Strength +1
            strength = strength + 1
         if (score1 or score2 == 2):  # Dexterity +1
            dexterity = dexterity + 1
         if (score1 or score2 == 3):  # Constitution +1
            constitution = constitution + 1
         if (score1 or score2 == 4):  # Intelligence +1
            intelligence = intelligence + 1
         if (score1 or score2 == 5):  # Wisdom +1
            wisdom = wisdom + 1
         if (score1 or score2 == 6):  # Charisma +1
            charisma = charisma + 1
      else:
         print('Increase an Ability by 2pts: 1Strength, 2Dexterity, 3Constitution, 4Intelligence, 5Wisdom, 6Charisma :')
         score1 = (input('Pick the number you would like to increase : '))
         file1.write(score1 + ' + 2' + '\n')
         if (score1 == 1):
            strength = strength + 2
         if (score1 == 2):
            dexterity = dexterity + 2
         if (score1 == 3):
            constitution = constitution + 2
         if (score1 == 4):
            intelligence = intelligence + 2
         if (score1 == 5):
            wisdom = wisdom + 2
         if (score1 == 6):
            charisma = charisma + 2
      file1.write('Spell 41 : ' + '\n')
      file1.write('Spell 42 : ' + '\n')

   if (c_level >= 20):     # Character is max level 20
      print('Level 20 : +6 Signature Spell, Spells ~ 5,4,3,3,3,3,2,2,1,1'+'\n')
      file1.write('\n')
      file1.write('Level 20 : '+'\n')
      file1.write('Signature Spell, Spell slots ~ 5,4,3,3,3,3,2,2,1,1' + '\n')
      file1.write('Spell 43 : ' + '\n')
      file1.write('Spell 44 : ' + '\n')
   str_mod = math.floor((int(strength) - 10) / 2.0)
   dex_mod = math.floor((int(dexterity) - 10) / 2.0)
   con_mod = math.floor((int(constitution) - 10) / 2.0)
   int_mod = math.floor((int(intelligence) - 10) / 2.0)
   wis_mod = math.floor((int(wisdom) - 10) / 2.0)
   chr_mod = math.floor((int(charisma) - 10) / 2.0)
   print('Strength = ' + str(strength) + ', STR modifier + ' + str(str_mod))
   file1.write('Strength = ' + str(strength) + ', STR modifier + ' + str(str_mod))
   print('Dexterity = ' + str(dexterity) + ', DEX modifier + ' + str(dex_mod))
   file1.write('Dexterity = ' + str(dexterity) + ', DEX modifier + ' + str(dex_mod))
   print('Constitution = ' + str(constitution) + ', CON modifier + ' + str(con_mod))
   file1.write('Constitution = ' + str(constitution) + ', CON modifier + ' + str(con_mod))
   print('Intelligence = ' + str(intelligence) + ', INT modifier + ' + str(int_mod))
   file1.write('Intelligence = ' + str(intelligence) + ', INT modifier + ' + str(int_mod))
   print('Wisdom = ' + str(wisdom) + ', WIS modifier + ' + str(wis_mod))
   file1.write('Wisdom = ' + str(wisdom) + ', WIS modifier + ' + str(wis_mod))
   print('Charisma = ' + str(charisma) + ', CHR modifier + ' + str(chr_mod))
   file1.write('Charisma = ' + str(charisma) + ', CHR modifier + ' + str(chr_mod))


   # closes file and frees up memory
   file1.close()
   print('Creating... ' + ((file_name)+'.txt')+"\n")
