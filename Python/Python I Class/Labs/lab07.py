for temp in range(-40,111,10) :
    ftemp = float(temp)

    if ( temp == 0 ) or ( temp == 50 ) :
        continue

    ctemp = (ftemp - 32) * 5 / 9
    print '%.1f degrees Fahrenheit is %.1f degrees Centrigrade' % (
        ftemp, ctemp)

    if ftemp > 95.0 :
        print "It's very hot!"
    elif ftemp > 80.0 and ftemp <= 95.0 :
        print "It's hot"
    elif ftemp > 60.0 and ftemp <= 80.0 :
        print "It's nice out"
    elif ftemp > 40.0 and ftemp <= 60.0 :
        print "It's chilly"
    else :
        print "It's cold!"
