def convert(input_ftemp) :
    converted_ctemp = (input_ftemp - 32) * 5 / 9
    return converted_ctemp

while True :
    temp = raw_input("What is the temperature in Fahrenheit? ")
    try :
        ftemp = float(temp)
    except ValueError :
        print 'Bad Data -', temp,' Try again.'
        continue
    else :
        ftemp = float(temp)
        ctemp = convert(ftemp)
        print '%.1f degrees Fahrenheit is %.1f degrees Centrigrade' % (
            ftemp, ctemp )
        break
