def sort_with_select(a_list):

    #For each index in the list...
    for i in range(len(a_list)):

        minIndex = i


        for j in range(i + 1, len(a_list)):

            if a_list[j] < a_list[minIndex]:
                minIndex = j

        minValue = a_list[minIndex]


        del a_list[minIndex]


        a_list.insert(i, minValue)


    return a_list

def inverted_sort(a_list):
    for i in range(len(a_list)):

        maxIndex = i


        for j in range(i + 1, len(a_list)):

            if a_list[j] > a_list[maxIndex]:
                maxIndex = j

        maxValue = a_list[maxIndex]


        del a_list[maxIndex]


        a_list.insert(i, maxValue)


    return a_list
