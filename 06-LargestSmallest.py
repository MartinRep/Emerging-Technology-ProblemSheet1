def smallLarge(theList):
    print(theList)
    #Loops through the list
    for i in range(0,theList.__len__()):
        #Assaign the initial values to smallest and largest
        if i == 0:
            smallest = theList[0]
            largest = theList[0]
        #Update the smallest if needed
        if smallest > theList[i]:
            smallest = theList[i]
        #Update the largest if needed
        if largest < theList[i]:
            largest = theList[i]
    #return the values
    return(smallest, largest)

#test
print(smallLarge([10,2,3,4,10,34,5,6,7]))
(smallest,largest) = smallLarge([10,2,3,4,10,34,5,6,7])
print("Largest: "+str(smallest)+" Smallest: "+str(largest))
