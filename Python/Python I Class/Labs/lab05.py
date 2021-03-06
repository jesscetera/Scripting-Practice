# Equitions to convert between F and C:
#     Fahrenheit = 9 / 5 * Centrigrade + 32
#     Centrigrade = 5 / 9 * (Fahrenheit - 32)

# Gathering current temp to convert
f_temp = raw_input("What is the temperature in Fahrenheit? ")
    #print "f_temp", f_temp # for debugging

# Converting the input string into a float
f_temp_float = float(f_temp)
    #print "f_temp_float", f_temp_float # for debugging

# Converting F to C
c_temp = (f_temp_float - 32) * 5 / 9
    #print "c_temp", c_temp # for debugging

# Without formatting
#print "The temperature is %s degrees Centrigrade." % (c_temp)

# Formatting to limit decimals to only 1
print '%.1f degrees Fahrenheit is %.1f degrees Centrigrade' % (
    f_temp_float, c_temp)

if f_temp_float > 95.0 :
    print "It's very hot!"
elif f_temp_float > 80.0 and f_temp_float <= 95.0 :
    print "It's hot"
elif f_temp_float > 60.0 and f_temp_float <= 80.0 :
    print "It's nice out"
elif f_temp_float > 40.0 and f_temp_float <= 60.0 :
    print "It's chilly"
else :
    print "It's cold!"
