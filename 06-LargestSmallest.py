def smallLarge(theList):
    print(theList)
    smallest = largest = None
    #Loops through the list, also prevent errors with empty list as it skips the for loop if list is empty
    for i in range(0,theList.__len__()):
        #Assaign the initial values to smallest and largest
        if i == 0:
            smallest = largest = theList[0]
        #Update the smallest if needed
        if smallest > theList[i]:
            smallest = theList[i]
        #Update the largest if needed
        if largest < theList[i]:
            largest = theList[i]
    #return the values
    return(smallest, largest)

#test
print(smallLarge([]))
(smallest,largest) = smallLarge([10,2,3,4,10,34,5,6,7])
print("Smallest: "+str(smallest)+" Largest: "+str(largest))
