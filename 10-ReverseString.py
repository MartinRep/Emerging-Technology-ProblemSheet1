#Adapted from https://stackoverflow.com/questions/931092/reverse-a-string-in-python#931095
def reverseString(strng):
    #string[start:stop:step]
    return strng[::-1]
#Test
print(reverseString("Repo"))