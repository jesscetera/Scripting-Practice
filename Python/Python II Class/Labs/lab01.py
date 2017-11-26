#lab01
from random import randrange as rr

#Functions!
#roll two dice and add them together
def dice_roll() :
	return rr(1,7) + rr(1,7)

#first roll outcome
def first_roll(dice_roll) :
	if (dice_roll == 2) or (dice_roll == 3) or (dice_roll == 12) :
		return lose #lost
	elif (dice_roll == 7) or (dice_roll == 11) :
		return win #win
	else :
		return contin

#subsequent rolls outcome
def sub_roll(dice_roll) :
	if dice_roll != 7 : 
		return win #win
	elif dice_roll == 7 :
		return lose #lost

#calculating updated money based on previous outcome
def money(outcome) :
	if outcome == win :
		return 20
	elif outcome == lose or contin :
		return 0

#initialized variables to play based on
current_money = 100
print "Begining Balance = ${0}".format(current_money)
rolls = 1
bet = -10
lose = "Lost!"
win = "Won!"
contin = "Continue"
keep_playing = True
rolls = 0

#script body!
while keep_playing :
	if rolls == 0 :
		rolls += 1
		current_money += bet
		dice_total = dice_roll()
		dice_outcome = first_roll(dice_total)
		current_money += money(dice_outcome)
		print "Balance = ${0} - {1} You {2}".format(current_money,dice_total,dice_outcome)
	
	elif rolls > 0 :
		current_money += bet
		if current_money <= 0 :
			keep_playing = False
		dice_total = dice_roll()
		dice_outcome = sub_roll(dice_total)
		current_money += money(dice_outcome)
		print "Balance = ${0} - {1} You {2}".format(current_money,dice_total,dice_outcome)
			
	print "Balance = ${0}".format(current_money),
	play_again = raw_input("Do you wish to play again? y/n ")
	if (play_again != 'y') and (play_again != 'Y') :
		keep_playing = False


