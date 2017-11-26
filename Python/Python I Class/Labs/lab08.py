header = 'Multiplication Table'
width = 26
print '{0:^26}'.format(header)
print '-' * width
for first in range(1,10):
    for second in range(1,10):
        print '{0:2d}'.format( first * second ),
    print
print '-' * width
