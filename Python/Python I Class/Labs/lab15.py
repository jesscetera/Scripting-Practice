# Initialized values
number_of_trees = 0
total_tree_height = 0
tallest_tree = 0
shortest_tree = 1000000
trees_over_300 = 0

# Opening data file and parsing contents
data_file = open('/Users/jessicawidener/scripts/python2/Python_I_Data/trees.dat', 'r')
for tree in data_file :
    try :
        tree_entry = float(tree)
    except ValueError :
        print '[!] Bad data found.'
        continue
    else :
        tree_entry = float(tree)
        number_of_trees += 1
        total_tree_height += tree_entry
        if tree_entry > tallest_tree :
            tallest_tree = tree_entry
        if tree_entry < shortest_tree :
            shortest_tree = tree_entry
        if tree_entry > 300 :
            trees_over_300 += 1
data_file.close()

# Reporting file contents to screen
print 'The total number of trees is : ''{}'.format( number_of_trees )
avg_height = total_tree_height / number_of_trees
print 'The average height of the trees is : ''{0:.1f}'.format( avg_height )
print 'The tallest tree is : ''{}'.format( tallest_tree )
print 'The shortest tree is : ''{}'.format( shortest_tree )
print 'The number of trees over 300 feet in height : ''{}'.format( trees_over_300 )

# Reporting file contents to file
report = open('/Users/jessicawidener/scripts/python2/Python_I_Data/trees_report.dat', 'w')
report.write('The total number of trees is : ''{}'.format( number_of_trees ) + '\n' )
report.write('The average height of the trees is : ''{0:.1f}'.format( avg_height ) + '\n' )
report.write('The tallest tree is : ''{}'.format( tallest_tree ) + '\n' )
report.write('The shortest tree is : ''{}'.format( shortest_tree ) + '\n' )
report.write('The number of trees over 300 feet in height : ''{}'.format( trees_over_300 ) + '\n' )
report.close()
print 'Wrote report to file trees_report.dat.'
