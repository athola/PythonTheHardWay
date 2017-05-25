import random

def main():
    print('I am thinking of a number between 1 and 20')
    guessingNumber()
    
def inputGuess():
    while True:
        print('Take a guess.')
        guess = input()
        if guess.isdigit():
            if int(guess) <= 20 and int(guess) >= 1:
                return int(guess)

def checkGuess(guess, theNumber):
    if guess < theNumber:
        print('Your guess is too low')
        return True
    elif guess > theNumber:
        print('Your guess is too high')
        return True
    else:
        return False

def guessingNumber():
    number = random.randint(1, 20)
    incorrect = True
    numberOfGuesses = 0
    while incorrect:
        yourGuess = inputGuess()
        guessIncorrect = checkGuess(yourGuess, number)
        incorrect = guessIncorrect
        numberOfGuesses += 1
    print('Good job! You guessed my number in ' + str(numberOfGuesses) + ' guesses!')
    
main()
