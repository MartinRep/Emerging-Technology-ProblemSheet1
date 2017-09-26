#Adapted from https://stackoverflow.com/questions/1720421/how-to-append-list-to-second-list-concatenate-lists#1720432
def mergeAndSort(firstList, secondList):
    #Merges two lists into one
    firstList.extend(secondList)
    #sort the list
    firstList.sort()
    return firstList
#Test
print(mergeAndSort([1,4,3,6],[3,6,8,9]))