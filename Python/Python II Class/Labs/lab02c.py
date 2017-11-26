#lab02c

#Using the chr() and ord() built-in functions, print the ASCII characters corresponding to the 
#numbers 32 through 126. 

for num in range(32,126):
	print chr(num),

#Then, from the string module, import the variable printable. 
from string import printable

#Afterwards, iterate through the "printable" string and print out each entry and its corresponding ordinal
print
for char in printable:
	print "{0!r} {1}".format(char, ord(char))