#Script to calculate fullness of the available cars based on hard coded numbers of people present.

#total cars
cars = 100
#total seats per car
seats = 4
#total people willing to drive
drivers = 30
#total people not willing to drive
passengers = 90

cars_not_driven = cars - drivers
cars_driven = drivers
carpool_capacity = cars_driven * seats
avg_passengers_per_car = (drivers + passengers) / cars_driven

print 'There are', cars , 'cars available.'
print 'There are only', drivers, 'drivers available.'
print 'There will be', cars_not_driven, 'empty cars today.'
print 'We can transport', carpool_capacity, 'people today.'
print 'We have', passengers, 'people to carpool today.'
print 'We need to put about', avg_passengers_per_car, 'in each car today.'
