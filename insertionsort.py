def insertion(alist):

    for i in range(1,len(alist)):
        new = alist[i]
        old = alist[i-1]
        if new < old:
            for j in range(0,i):
                if alist[j]>new:
                    del alist[i]
                    alist.insert(j, new)
                    break
    return alist
