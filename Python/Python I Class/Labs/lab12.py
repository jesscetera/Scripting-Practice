def convert(input_ftemp) :
    converted_ctemp = (input_ftemp - 32) * 5 / 9
    return converted_ctemp

while True :
    temp_file = open('/Users/jessicawidener/scripts/python2/Python_I_Data/temps.dat', 'r')
    for line in temp_file :
    #    print '{0}'.format(line)
        try :
            ftemp = float(line)
        except ValueError :
            print 'Data was not a number. Try again.'
            continue
        else :
            ftemp = float(line)
            ctemp = convert(ftemp)
            print '%.1f degrees Fahrenheit is %.1f degrees Centrigrade' % (
                ftemp, ctemp )
            continue
    temp_file.close()
    break
