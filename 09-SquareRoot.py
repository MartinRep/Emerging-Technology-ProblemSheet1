import math
def SquareRoot(x, margin):
    z = 1
    #Sets the last Z calculated
    lastZ = None
    #Initialize the while condition value
    found = False
    #While loop until Z and previous Z are equal with margin in mind
    while found == False:
        #Update the lastZ with current Z value
        lastZ = z
        #Calculate the next Z from Newton Square Root method
        z = z - ((z*z - x) / (2 * z))
        #print(z)
        #Check if Z is changing more the defined in margin variable
        if (z <= lastZ+margin) and (z >= lastZ-margin): found = True
    return z
    
#Test
result = SquareRoot(250,0.5)
mathResult = math.sqrt(250)
print("Function: "+str(result)+" Math,sqrt: "+str(mathResult)+" Difference: "+str(result - mathResult))
