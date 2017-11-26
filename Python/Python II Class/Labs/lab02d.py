#lab02d

#Read the entire book "Alice in Wonderland" into memory. 
data_file = open('/Users/jessicawidener/Projects/python/PythonII/Python_II_Data/alice_in_wonderland.dat')
book = data_file.read().lower()

#Find the words caterpillar and gryphon. 
word1 = 'caterpillar'
word2 = 'gryphon'

#Print the location of the first occurrence of each word. 
print "First {0} {1}".format(word1,book.find(word1))
print "First {0} {1}".format(word2,book.find(word2))

#Also, print the number of times each word occurs in the book.
print "Count {0} {1}".format(word1,book.count(word1))
print "Count {0} {1}".format(word2,book.count(word2))

#Determine the location of the last occurrence of each word. There is a method that will do this for you.
print "Last {0} {1}".format(word1,book.rfind(word1))
print "Last {0} {1}".format(word2,book.rfind(word2))