from random import randrange as rr
goal = rr(100)
print goal #for debug
attempts = 0

while True :
    temp = raw_input('Enter your guess: ')
    guess = int(temp)
    attempts += 1
    if guess < goal :
        print 'Incorrect! Your guess is too low'
    elif guess > goal :
        print 'Incorrect! Your guess is too high'
    else :
        print 'Your guess is correct!'
        print 'You succeeded in {0:d} attempts!'.format(attempts)
        break
