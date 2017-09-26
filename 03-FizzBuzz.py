#Loop from 0 to 100
for i in range(100):
    #If number is multiples of 5 and 3
    if i%3 == 0 and i%5 == 0:
        print ("FizzBuzz")
    #if number is multiples of 3
    elif i%3 == 0:
        print ("Fizz")
    #if number is multiple of 5
    elif i%5 == 0:
        print ("Buzz")
    #prints out the number which are not Fizz or Buzz
    else:
        print (i)