def are_anagrams(str1, str2):
    str1dict = {}
    str2dict = {}
    for i in str1:
        if ord(i) >= 97 and ord(i) <= 122 or (ord(i) >= 65 and ord(i) <= 90):
            if i.lower() not in str1dict:
                str1dict[i.lower()] = 0
            str1dict[i.lower()] += 1
    for i in str2:
        if ord(i) >= 97 and ord(i) <= 122 or (ord(i) >= 65 and ord(i) <= 90):
            if i.lower() not in str2dict:
                str2dict[i.lower()] = 0
            str2dict[i.lower()] += 1
    if len(str1dict) == len(str2dict) and len(str1dict) > 0:
        for i in str1dict:
            if i in str2dict and str1dict[i] == str2dict[i]:
                continue
            else:
                return False
    else:
        return False
    return True

#This problem can also be done in multiple ways.
#Firstly, because we are told not to consider spaces and capitalization
#we change our input strings to lower and remove all our spaces.

def are_anagrams(first_word, second_word):
    first_word = first_word.lower()
    second_word = second_word.lower()
    first_word = first_word.replace(' ', '')
    second_word = second_word.replace(' ', '')

#For me, the first thought was to store the letters of the first word
#into a list and then iterate through the second word and remove the letter stored
#if it existed in the list.

#SO, I create an empty list called 'letters'

    letters = []

#I then iterate through my first word and the append all the characters

    for char in first_word:
        letters.append(char)

#I then iterate through my second word and see if the letter I am currently
#iterating through is in my list.
#If it is in my list, then I remove that character (this avoids duplicates)
#and if my current letter is not in my list then I automatically return False
#since that means my second word has a letter that my first word doesn't!

    for char in second_word:
        if char not in letters:
            return False
        letters.remove(char)

#At the very end when we are done iterating through, I return the boolean value
#of whether my length of list is equal to 0. I do not simply return True because
#there may be cases where my first word will have letters that my second letter
#might not have. ie. first = hello, second = helo (list would still contain 'l')

    return len(letters) == 0
