#lab3a - Probability

from random import randrange as rr
roll_lst = 13 * [0]
poss_outcome = range(2,13)
total_rolls = 0

#Create a function to simulate the rolling of a pair of dice. 
def dice_roll() :
	return rr(1,7) + rr(1,7)

#Call this function 100,000 times accumulating the results of each roll in a list. 
goal_rolls = 100000
for num in range(goal_rolls):
	roll = dice_roll()
	roll_lst[roll] += 1

#Print the percentage of times each possible roll occurred along with the total number of rolls. 
for num in poss_outcome:
	print "Total {0}'s: {1:,d} or {2:.2f}%".format(num,roll_lst[num], roll_lst[num]*100.0/goal_rolls)