#Recursive function for calculating Factorial
def factorial(x):
    #if end of the factorial, then starts calling back
    if x == 1: return x
    else: return factorial(x-1)*x
#Test
sumNumber=0
#Gets and converts the result of (int) factorial into String
result = str(factorial(100))
print ("Factorial of 100: "+result)
#Loops through the String char by char. Converts it to the Integer and add it to the sumNumbre variable
for i in range(0, len(result)):
    sumNumber += int(result[i])
#Prints out the sum result
print("Sum of Factorial(100): "+str(sumNumber))