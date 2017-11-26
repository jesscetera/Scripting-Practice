print 'Opening the file...'
target = open('/Users/jessicawidener/scripts/python2/lab14.txt', 'w')

line1 = 'First line.'
line2 = 'Second line.'
line3 = 'Third line.'

print "I'm going to write these to a file."

target.write(line1)
target.write("\n")
target.write(line2)
target.write("\n")
target.write(line3)
target.write("\n")

print 'And finally, we close it.'
target.close()
