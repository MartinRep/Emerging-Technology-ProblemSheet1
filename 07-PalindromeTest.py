def palindromeTest(word):
    #loops through string from both sides
    for i in range(0,int(len(word)/2)):
        #print(word[i]+" "+word[-(i+1)]+" i: "+str(i))
        #if any of the characters on oposite positions are not equal the String fails Palindrome Test
        if word[i] != word[-(i+1)]:
            return False
    #if loop loops through tge string with coresponding characters equal the String passes the Test
    return True

#Test
print(palindromeTest("kokotirtokok"))
print(palindromeTest("radar"))