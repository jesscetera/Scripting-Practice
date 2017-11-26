# Lab 17 :
# Use the randrange function in the random module to simulate rolling a pair of dice. 
# Simulate 1000 rolls and calculate the percentage of the rolls that are sevens and the percentage of the rolls that are twos. 

from random import randrange as rr
begin_rolls = 0
end_rolls = 1000
one = 0
two = 0
three = 0
four = 0
five = 0
six = 0
seven = 0
eight = 0
nine = 0
ten = 0 
eleven = 0
twelve = 0

# Function for rolling two six-sided dice and adding their outputs together.
def roll_dice():
	first = rr(6)
	second = rr(6)
	return first, second

# Loop to roll dice until 1000 rolls have been made. 
# Roll total should be enumerating a previously intilized possible total outcome.
while begin_rolls <= end_rolls :
	first, second = roll_dice()
	# Print lines for debugging
	dice_total = first + second
	# print(first)
	# print (second)
	# print "Current Roll is %s " % ( begin_rolls )
	if dice_total == 1 :
		one +=1
		begin_rolls +=1
		continue
	elif dice_total == 2 :
		two +=1
		begin_rolls +=1
		continue
	elif dice_total == 3 :
		three +=1
		begin_rolls +=1
		continue
	elif dice_total == 4 :
		four +=1
		begin_rolls +=1
		continue
	elif dice_total == 5 :
		five +=1
		begin_rolls +=1
		continue
	elif dice_total == 6 :
		six +=1
		begin_rolls +=1
		continue
	elif dice_total == 7 :
		seven +=1
		begin_rolls +=1
		continue
	elif dice_total == 8 :
		eight +=1
		begin_rolls +=1
		continue
	elif dice_total == 9 :
		nine +=1
		begin_rolls +=1
		continue
	elif dice_total == 10 :
		ten +=1
		begin_rolls +=1
		continue
	elif dice_total == 11 :
		eleven +=1
		begin_rolls +=1
		continue
	elif dice_total == 12 :
		twelve +=1	
		begin_rolls +=1
		continue

percent_two = ( float(two) / end_rolls ) * 100
percent_seven = ( float(seven) / end_rolls ) * 100
print "Percentage of 2's : {0}%".format(percent_two)
print "Percentage of 7's : {0}%".format(percent_seven)
