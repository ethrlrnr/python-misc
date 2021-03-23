def sort_with_bubbles(lst):
    #Set swap_occurred to True to guarantee the loop runs once
    swap_occurred = True

    #Run the loop as long as a swap occurred the previous time
    while swap_occurred:

        #Start off assuming a swap did not occur
        swap_occurred = False

        #For every item in the list except the last one...
        for i in range(len(lst) - 1):

            #If the item should swap with the next item...
            if lst[i] > lst[i + 1]:

                #Then, swap them! But these lines aren't
                #quite right: fix this code!
                temp = lst[i]
                lst[i] = lst[i + 1]
                lst[i + 1] = temp

                #One more line is needed here; add it!
                swap_occurred = True
    return lst
