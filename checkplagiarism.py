def check_plagiarism(afile1, afile2):
    myF1 = open(afile1, "r")
    myF2 = open(afile2, "r")

    list1 = myF1.read().split()
    list2 = myF2.read().split()
    myF1.close()
    myF2.close()
    resList = []
    resIndex = 0

    for i in range(len(list1)):
        for h in range(len(list2)):

            count = 0
            if list1[i] == list2[h]:
                resList.append([])
                found = True
                while found and i+count < len(list1) and h+count<len(list2):
                    if list1[i+count] == list2[h+count]:
                        found = True
                        resList[resIndex].append(list1[i+count])
                    else:
                        found = False
                    count += 1
                if len(resList[resIndex])>=5:
                    resIndex += 1
                else:
                    del resList[resIndex]

    if len(resList) == 0:
        return False
    else:
        maxIndex = 0
        maxSize = 0
        for i in range(len(resList)):
            if len(resList[i])> maxSize:
                maxIndex = i
                maxSize = len(resList[i])
        resStr = ""
        for word in resList[maxIndex]:
            resStr += word + " "

    return resStr[:-1]
