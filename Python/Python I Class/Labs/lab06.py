while True :
    f_temp = raw_input("What is the temperature in Fahrenheit? ")

    if ( f_temp == 'q' ) or ( f_temp == 'Q' ) :
        break

    else :
        f_temp_float = float(f_temp)
        c_temp = (f_temp_float - 32) * 5 / 9
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
