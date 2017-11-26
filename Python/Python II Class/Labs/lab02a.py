"""Lab02a

In your data folder, you will find a file containing the text for the book, Alice in Wonderland. 
Read the entire file into memory. Using only the tools we have covered so far, scan this text 
counting all of the letters regardless of case. Keep a separate count for all occurrences of the 
letter 'e' again regardless of case. At the end, print the total of all letters, the number of e's
and the percent of the total that the 'e's comprise.
"""

data_file = open('/Users/jessicawidener/Projects/python/PythonII/Python_II_Data/alice_in_wonderland.dat')
book_data = data_file.read().lower()
tot_char = 0

for char in book_data :
	if char.isalpha() :
		tot_char += 1

print "Total Characters: {0:,d}".format(tot_char)

tot_e = book_data.count('e')
print "Total Number of E's: {0:,d}".format(tot_e)

per_e = (100.00 * tot_e) / tot_char
print "Percentage of E's: {0:.2f}%".format(per_e)