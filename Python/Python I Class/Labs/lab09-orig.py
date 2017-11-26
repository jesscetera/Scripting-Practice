from random import randrange as rr
goal = rr(100)
print goal #for debug
attempts = 0

guess = raw_input('Enter your guess: ')

while guess != goal :
        if guess < goal :
                print 'Incorrect! Your guess is too low'
                attempts += 1
                print attempts #for debug
        guess = raw_input('Enter your guess: ')

        elif guess > goal :
                print 'Incorrect! Your guess is too high'
                attempts += 1
                print attempts #for debug
        guess = raw_input('Enter your guess: ')

print 'Your guess is correct!'
print 'You succeeded in %s attempts!' % (attempts)
