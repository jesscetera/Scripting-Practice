"""lab02b

Review the file tmpprecip2012.dat. It is laid out as follows: 
Columns Content
1 - 2 	Month
3 - 4 	Day
5 - 8 	Year
9 - 13 	Precipitation in the format dd.dd (inches) 
14 - 16 High Temperature
The file contains temperature and precipitation data for 2012. 
Accumulate the number of days with measurable precipitation and the precipitation total 
for the year and print them out.
"""

tot_precip = 0
tot_days = 0
data_file = open('/Users/jessicawidener/Projects/python/PythonII/Python_II_Data/tmpprecip2012.dat')

for line in data_file :
	precip = float(line[8:13])
	if precip != 0 :
		tot_days += 1
		tot_precip += precip

print "Total Rain: \n{0} days \n{1:.2f} inches".format(tot_days,tot_precip)