def convert(input_ftemp) :
    converted_ctemp = (input_ftemp - 32) * 5 / 9
    return converted_ctemp

ftemp = float(raw_input("What is the temperature in Fahrenheit? ") )
ctemp = convert(ftemp)
print '%.1f degrees Fahrenheit is %.1f degrees Centrigrade' % (
    ftemp, ctemp )
