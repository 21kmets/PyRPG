# Python3 code to demonstrate working of
# Selective key values in dictionary
# Using list comprehension + get()

# Initialize dictionary

s1 = {
    'i_name': 'dagger',
    'dc_craft': 13,
    'fe_weight': 1,
    'total_weight': 1,
    'c_t_cost': 1,
    'c_g_cost': 1,
    'pp': 2.0,
    'dmg': '1d4',
    'prop': 'piercing, simple, finesse, light, thrown (range 20/60)'
}
s2 = {
    'i_name': 'handaxe',
    'dc_craft': 13,
    'fe_weight': 2,
    'total_weight': 2,
    'c_t_cost': 1,
    'c_g_cost': 2.5,
    'pp': 5.0,
    'dmg': '1d6',
    'prop': 'slashing, simple, light, thrown (range 20/60)'
}
s3 = {
    'i_name': 'spear',
    'dc_craft': 13,
    'fe_weight': 3,
    'total_weight': 3,
    'c_t_cost': 1,
    'c_g_cost': 0.5,
    'pp': 1.0,
    'dmg': '1d6',
    'prop': 'piercing, simple, versatile(1d8), thrown (range 20/60)'
}
s4 = {
    'i_name': 'arrows',
    'dc_craft': 13,
    'fe_weight': 1,
    'total_weight': 1,
    'c_t_cost': 1,
    'c_g_cost': 1,
    'pp': 1.0,
    'prop': 'pp = 1 gp for 20 arrows 1 lb total weight, can craft arrows equal to STR score per day'
}
s3 = {
    'i_name': 'dagger',
    'dc_craft': 13,
    'fe_weight': 1,
    'total_weight': 1,
    'c_t_cost': 1,
    'c_g_cost': 1,
    'pp': 2.0,
    'dmg': '1d4',
    'prop': 'piercing, simple, finesse, light, thrown (range 20/60)'
}
s3 = {
    'i_name': 'dagger',
    'dc_craft': 13,
    'fe_weight': 1,
    'total_weight': 1,
    'c_t_cost': 1,
    'c_g_cost': 1,
    'pp': 2.0,
    'dmg': '1d4',
    'prop': 'piercing, simple, finesse, light, thrown (range 20/60)'
}
s3 = {
    'i_name': 'dagger',
    'dc_craft': 13,
    'fe_weight': 1,
    'total_weight': 1,
    'c_t_cost': 1,
    'c_g_cost': 1,
    'pp': 2.0,
    'dmg': '1d4',
    'prop': 'piercing, simple, finesse, light, thrown (range 20/60)'
}
s3 = {
    'i_name': 'dagger',
    'dc_craft': 13,
    'fe_weight': 1,
    'total_weight': 1,
    'c_t_cost': 1,
    'c_g_cost': 1,
    'pp': 2.0,
    'dmg': '1d4',
    'prop': 'piercing, simple, finesse, light, thrown (range 20/60)'
}
s3 = {
    'i_name': 'dagger',
    'dc_craft': 13,
    'fe_weight': 1,
    'total_weight': 1,
    'c_t_cost': 1,
    'c_g_cost': 1,
    'pp': 2.0,
    'dmg': '1d4',
    'prop': 'piercing, simple, finesse, light, thrown (range 20/60)'
}
s3 = {
    'i_name': 'dagger',
    'dc_craft': 13,
    'fe_weight': 1,
    'total_weight': 1,
    'c_t_cost': 1,
    'c_g_cost': 1,
    'pp': 2.0,
    'dmg': '1d4',
    'prop': 'piercing, simple, finesse, light, thrown (range 20/60)'
}
s3 = {
    'i_name': 'dagger',
    'dc_craft': 13,
    'fe_weight': 1,
    'total_weight': 1,
    'c_t_cost': 1,
    'c_g_cost': 1,
    'pp': 2.0,
    'dmg': '1d4',
    'prop': 'piercing, simple, finesse, light, thrown (range 20/60)'
}

# Using list comprehension + get()
# Selective key values in dictionary
# res = [s1.get(key) for key in key_list]

crafting = 'Y'
strength = int(input('What is your Strength Score? '))
str_mod = (int(round((strength - 10)/2)))

while (crafting == 'Y'):
# read in input from keyboard for
    crafting = input('Would you like to craft an item? [Y,n]: ')
    sx = input('\n Enter the name of the item you want to craft? : ')
    qa = input('\n Scrap, Common or Mastercraft quality? [S,C,M]: ')


# printing result

    if ((s1.get('i_name')) == (sx)):
        print(s1.get('c_cost'))   # float value for crafting cost
        print(s1.get('craft_dc'))   # int value for DC crafting check
        print(s1.get('c_time'))   # int value for estimated crafting time
    elif ((s2.get('i_name')) == (sx)):
        print(s2.get('c_cost'))   # float value for crafting cost
        print(s2.get('craft_dc'))   # int value for DC crafting check
        print(s2.get('c_time'))   # int value for estimated crafting time
    elif ((s3.get('i_name')) == (sx)):
        print(s3.get('c_cost'))   # float value for crafting cost
        print(s3.get('craft_dc'))   # int value for DC crafting check
        print(s3.get('c_time'))   # int value for estimated crafting time
    else:
        print('not an item')




# Set up a dictionary using {}

# S2 = {'dagger': ['Y', 'simple', 1.0, 1, 13, 1, 1.0, 'NP']}
# S3 = {'handaxe': ['Y', 'simple', 2.0, 1, 13, 1, 2.5, 'NP']}
#  S4 = {'darts': ['Y', 'simple', 0.25, 1, 13, 1, 0.02, 'SP']}



# looping though the dictory by keynames, values, and items

# print("\n all key names in the dictionary, one by one:")
#for x in s1:
#    print(x)

#print('\n print the values')
#for x in s1:
#    print(s1[x])
#print('\n You can also use the values() function to return values of a dictionary:')
#for x in s1.values():
#    print(x)

#print('\n Loop through both keys and values, by using the items() function:')
#for x, y in s1.items():
#    print(x, y)
