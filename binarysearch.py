def binary_search(searchList, searchTerm):

    #First, the list must be sorted.
    searchList.sort()

    #Now, each iteration of the loop, we want to narrow
    #down the part of the list to look at. So, we need to
    #keep track of the range we've narrowed down to so
    #far. Initially, that will be the entire list, from
    #the first index to the last.

    min = 0
    max = len(searchList) - 1

    #Now, we want to loop as long as our range has any
    #numbers left to investigate. As long as there is
    #more than one number between minimum and maximum,
    #we're not done searching.

    while min <= max:

        #We want to check the middle item of the
        #current range, which is the average of the
        #current minimum and maximum index. For
        #example, if min was 5 and max was 15, our
        #middle number would be at index 5. We'll
        #use floor division because indices must be
        #integers.
        currentMiddle = (min + max) // 2

        #If the term in the middle is the term we're
        #looking for, we're done!
        if searchList[currentMiddle] == searchTerm:
            return True

        #If not, we want to check if the term we're
        #looking for should come earlier or later.

        #If the term we're looking for is less than
        #the current middle, then search the first
        #half of the list:
        elif searchTerm < searchList[currentMiddle]:
            max = currentMiddle - 1

        #If the term we're looking for is greater
        #than the current middle, search the second
        #half of the list:
        else:
            min = currentMiddle + 1

        #Each iteration of the loop, one of three
        #things happens: the term is found, max
        #shrinks, or min grows. Eventually, either
        #the term will be found, or min will be
        #equal to max.

    #If the search term was found, this line will
    #never be reached because the return statement
    #will end the function. So, if we get this
    #far, then the search term was not found, and
    #we can return False.
    return False

def binary_search(searchList, searchTerm):

    #First, the list must be sorted.
    searchList.sort()

    #With each recursive call to binary_search, the size
    #of the list will be cut in half, rounding down. If
    #the search term is not found, then eventually an
    #empty list will be passed into binary_search. So,
    #if searchList is empty, we know that the search
    #term was not found, and we can return False. This
    #is the base case for the recursive binary_search.

    if len(searchList) == 0:
        return False

    #If there are still items in the list, then we want
    #to find if searchTerm is greater than, less than,
    #or equal to the middle term in the list. For that,
    #we need the index of the middle term.

    middle = len(searchList) // 2

    #First, the easy case: if it's the middle term, we
    #found it! Return True.
    if searchList[middle] == searchTerm:
        return True

    #If the search term is less than the middle term,
    #then repeat the search on the left half of the
    #list.
    elif searchTerm < searchList[middle]:
        return binary_search(searchList[:middle], searchTerm)

    #If the search term is greater than the middle
    #term, then repeat the search on the right half
    #of the list.
    else:
        return binary_search(searchList[middle + 1:], searchTerm)

from datetime import date


#Write your code here!
def binary_search_year(searchList, searchTerm):
    #First, the list must be sorted.
    searchList.sort()

    #With each recursive call to binary_search, the size
    #of the list will be cut in half, rounding down. If
    #the search term is not found, then eventually an
    #empty list will be passed into binary_search. So,
    #if searchList is empty, we know that the search
    #term was not found, and we can return False. This
    #is the base case for the recursive binary_search.

    if len(searchList) == 0:
        return False

    #If there are still items in the list, then we want
    #to find if searchTerm is greater than, less than,
    #or equal to the middle term in the list. For that,
    #we need the index of the middle term.

    middle = len(searchList) // 2

    #First, the easy case: if it's the middle term, we
    #found it! Return True.
    if searchList[middle].year == searchTerm:
        return True

    #If the search term is less than the middle term,
    #then repeat the search on the left half of the
    #list.
    elif searchTerm < searchList[middle].year:
        return binary_search_year(searchList[:middle], searchTerm)

    #If the search term is greater than the middle
    #term, then repeat the search on the right half
    #of the list.
    else:
        return binary_search_year(searchList[middle + 1:], searchTerm)
