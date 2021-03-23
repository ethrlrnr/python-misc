def mergesort(lst):

    #Then, what does it do? mergesort should recursively
    #run mergesort on the left and right sides of lst until
    #it's given a list only one item. So, if lst has only
    #one item, we should just return that one-item list.

    if len(lst) <= 1:
        return lst

    #Otherwise, we should call mergesort separately on the
    #left and right sides. Since each successive call to
    #mergesort sends half as many items, we're guaranteed
    #to eventually send it a list with only one item, at
    #which point we'll stop calling mergesort again.
    else:

        #Floor division on the length of the list will
        #find us the index of the middle value.
        midpoint = len(lst) // 2

        #lst[:midpoint] will get the left side of the
        #list based on list slicing syntax. So, we want
        #to sort the left side of the list alone and
        #assign the result to the new smaller list left.
        left = mergesort(lst[:midpoint])

        #And same for the right side.
        right = mergesort(lst[midpoint:])

        #So, left and right now hold sorted lists of
        #each half of the original list. They might
        #each have only one item, or they could each
        #have several items.

        #Now we want to compare the first items in each
        #list one-by-one, adding the smaller to our new
        #result list until one list is completely empty.

        newlist = []
        while len(left) and len(right) > 0:

            #If the first number in left is lower, add
            #it to the new list and remove it from left
            if left[0] < right[0]:
                newlist.append(left[0])
                del left[0]

            #Otherwise, add the first number from right
            #to the new list and remove it from right
            else:
                newlist.append(right[0])
                del right[0]

        #When the while loop above is done, it means
        #one of the two lists is empty. Because both
        #lists were sorted, we can now add the remainder
        #of each list to the new list. The empty list
        #will have no items to add, and the non-empty
        #list will add its items in order.

        newlist.extend(left)
        newlist.extend(right)

        #newlist is now the sorted version of lst! So,
        #we can return it. If this was a recursive call
        #to mergesort, then this sends a sorted half-
        #list up the ladder. If this was the original
        #call, then this is the final sorted list.

        return newlist

def sort_with_merge(lst):
    if len(lst) <= 1:
        return lst
    else:
        midpoint = len(lst) // 2
        left = sort_with_merge(lst[:midpoint])
        right = sort_with_merge(lst[midpoint:])
        newlist = []
        while len(left) and len(right) > 0:

            if left[0] < right[0]:
                newlist.append(right[0])
                del right[0]

            else:
                newlist.append(left[0])
                del left[0]
        newlist.extend(left)
        newlist.extend(right)
        return newlist

#Iterative

def mergeSort(a):

    current_size = 1

    # Outer loop for traversing Each
    # sub array of current_size
    while current_size < len(a) - 1:

        left = 0
        # Inner loop for merge call
        # in a sub array
        # Each complete Iteration sorts
        # the iterating sub array
        while left < len(a)-1:

            # mid index = left index of
            # sub array + current sub
            # array size - 1
            mid = min((left + current_size - 1),(len(a)-1))

            # (False result,True result)
            # [Condition] Can use current_size
            # if 2 * current_size < len(a)-1
            # else len(a)-1
            right = ((2 * current_size + left - 1,
                    len(a) - 1)[2 * current_size
                        + left - 1 > len(a)-1])

            # Merge call for each sub array
            merge(a, left, mid, right)
            left = left + current_size*2

        # Increasing sub array size by
        # multiple of 2
        current_size = 2 * current_size

# Merge Function
def merge(a, l, m, r):
    n1 = m - l + 1
    n2 = r - m
    L = [0] * n1
    R = [0] * n2
    for i in range(0, n1):
        L[i] = a[l + i]
    for i in range(0, n2):
        R[i] = a[m + i + 1]

    i, j, k = 0, 0, l
    while i < n1 and j < n2:
        if L[i] > R[j]:
            a[k] = R[j]
            j += 1
        else:
            a[k] = L[i]
            i += 1
        k += 1

    while i < n1:
        a[k] = L[i]
        i += 1
        k += 1

    while j < n2:
        a[k] = R[j]
        j += 1
        k += 1
