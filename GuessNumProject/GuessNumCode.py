import random

#def is basically making a function and calling it "guess", I would assume that is is pretty generic
def guess(n):
    randNum = random.randint(1,n)
    guess = 0
    while guess != randNum:
        guess = int(input(f'Guess a number between 1 and {n}: '))
        print(guess)

guess(10)