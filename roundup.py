import math

# round the 2.2 up to the nearest integer
print(int(math.ceil(2.2)))

# round the result down to the nearest integer
print(int(round(5/2)))


# Calculate the strength modifier for 15
strength = 15
print(int(round((strength - 10)/2)))


# Calculate crafting time for items
# Simple: c_time = W/4 round up minimum 1 day   base craft_DC = 13
# Moderate: c_time = W/2 round up minimum 1 day   base craft_DC = 14
# Complex: c_time = W round up minimum 1 day   base craft_DC = 15
#
# Scrap: costs 0.5 of purchase price, requires no craft checks -1 to ATK -1 to AC
# Common: costs 0.5 of purchase price,
# Mastercraft: costs 3x common, takes 25% longer, +8 to the base DC_craft check
mc_dc_mod = 8  # Mastercraft adds 8 to the base DC_craft check
#
fe_weight = 4   # variable for storing the weight of the iron
mc_t_mod = [1, 1.25]    # Mastercraft takes 25% longer to craft
smc_mod = [4.0, 2.0, 1.0]  # depending on if it's Simple, Moderate or Complex
# c_t_cost   ~ the variable for storing the cost in days to craft the item
print(int(math.ceil(fe_weight/smc_mod[1])*mc_t_mod[1]))    # 2d Moderately complex Mastercraft
print(int(math.ceil(fe_weight/smc_mod[0])*mc_t_mod[0]))   # 1d Simple ~ Common or Scrap
print(int(math.ceil(fe_weight/smc_mod[2])*mc_t_mod[1]))  # 5d Complex Mastercraft
print(int(math.ceil(fe_weight/smc_mod[0])*mc_t_mod[1]))   # 1d Simple Mastercraft

# You need to make a crafting check every 7 days you spend crafting, ie. 9days of crafting = 2 checks
# Craft checks are assumed to happen at the end of seven days or on the day you complete the item.
# If you fail a craft check while working towards Mastercraft it becomes Common.
# If you fail a craft check while working towards Common, you have one more chance to save it.
# On your next check you have disadvantage on the check, if you fail or have no more craft checks,
# it becomes Scrap.   # If you fail a roll you can not spend those days working on something else.
# When crafting an item you need at least 6 hours to dedicate to your work. If you spend
# more time than that, your GM can determine if you speed up progress on your crafting
# but the number of checks remains the same

# Calculate crafting cost in gold
# Scrap: costs *0.5 of purchase price : mc_g_mod[0]
# Common: costs *0.5 of purchase price : mc_g_mod[0]
# Mastercraft: costs 3x as much as crafting common or *1.5 of purchase price : mc_g_mod[1]
#
mc_g_mod = [1, 3.0]    # Mastercraft takes 3x more gold to craft than Scrap or Common
pp = 5     # cost of purchasing the item new
c_g_cost = (pp * mc_g_mod[1])     # cost of attempting to Mastercraft the same item