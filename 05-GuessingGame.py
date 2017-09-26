#Adapted from https://docs.scipy.org/doc/numpy/user/basics.creation.html
import random as random
guesses = []
correntGuess = False
magicNumber = random.randrange(0,100)
print(magicNumber)
while correntGuess != True:
    guess = input("Guess the magic number: ")    
    if guesses.__len__() == 0 :
        guesses.append(int(guess))
        print(guesses)
    elif guesses[-1] != int(guess):
        guesses.append(int(guess))
        print(guesses)
    if magicNumber == int(guess):
        correntGuess = True
    elif int(guess) > magicNumber:
        print("Your guess is high")
    elif int(guess) < magicNumber:
        print("Your guess is low")
print("That's the magic number! Congratulation!")        
print("Number of attempts: "+str(guesses.__len__()))