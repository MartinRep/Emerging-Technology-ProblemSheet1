#Adapted from http://www.effbot.org/pyfaq/how-do-i-generate-random-numbers-in-python.htm
#             https://stackoverflow.com/questions/1712227/how-to-get-the-size-of-a-list#1712236
import random as random
#List of guesses
guesses = []
correntGuess = False
#Magic number is generated as a random number between 0 and 100
magicNumber = random.randrange(0,100)
print("The magic number is number between 0 and 100")
#for development purposes
#print (magicNumber)
while correntGuess != True:
    guess = input("Guess the magic number: ")    
    #List is empty adds guess
    if guesses.__len__() == 0 :
        guesses.append(int(guess))
    #Checks if last guess is not the same as current one and only then the counter of guesses is updated
    elif guesses[-1] != int(guess):
        guesses.append(int(guess))
    #Correct quess end the while loop
    if magicNumber == int(guess):
        correntGuess = True
    #Displays guess hint
    elif int(guess) > magicNumber:
        print("Your guess is high")
    elif int(guess) < magicNumber:
        print("Your guess is low")
#After correct guess prints out congratulation and size of the list of guesses to display number of attempts
print("That's the magic number! Congratulation!")        
print("Number of attempts: "+str(guesses.__len__()))