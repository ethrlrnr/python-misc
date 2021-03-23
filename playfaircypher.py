CIPHER = (("D", "A", "V", "I", "O"),
          ("Y", "N", "E", "R", "B"),
          ("C", "F", "G", "H", "K"),
          ("L", "M", "P", "Q", "S"),
          ("T", "U", "W", "X", "Z"))



#Add your code here!

def find_letter(aletter):
    for i in range(len(CIPHER)):
        for j in range(len(CIPHER[i])):
            if aletter == CIPHER[i][j]:
                return (i, j)

def prepare_string(astr):
    res = astr.upper()
    res = res.replace("J","I")
    resTmp = ""
    for c in res:
        if ord(c) >= 65 and ord(c) <= 90:
            resTmp += c
    res = resTmp
    resTmp = ""
    if len(res) % 2 != 0:
        res += "X"
    for i in range(0,len(res),2):
        left = ""
        right = ""

        # Same Case
        if res[i+1] == res[i]:
            left = res[i]
            right = "X"
        else:
            left = res[i]
            right = res[i+1]
        resTmp += left + right + " "

    resTmp = resTmp[:-1]
    res = resTmp
    return res

def encrypt(astr):
    res = prepare_string(astr)
    resList = res.split()
    resTmp = ""
    for i in resList:
        rowL, columnL = find_letter(i[0])
        rowR, columnR = find_letter(i[1])

        # Row Case
        if rowL == rowR:
            newColL = columnL+1
            if newColL == len(CIPHER[rowL]):
                newColL = 0
            newColR = columnR+1
            if newColR == len(CIPHER[rowR]):
                newColR = 0
            resTmp += (CIPHER[rowL])[newColL] + CIPHER[rowR][newColR]

        # Rectangle Case
        if rowL != rowR and columnL != columnR:
            newColL = columnR
            newColR = columnL
            resTmp += (CIPHER[rowL])[newColL] + CIPHER[rowR][newColR]

        # Column Case

        if columnL == columnR:
            newRowL = rowL+1
            if newRowL == len(CIPHER[columnL]):
                newRowL = 0
            newRowR = rowR+1
            if newRowR == len(CIPHER[columnR]):
                newRowR = 0
            resTmp += (CIPHER[newRowL])[columnL] + CIPHER[newRowR][columnR]
    res = resTmp

    return res


def decrypt(astr):
    resTmp = ""
    for i in range(0,len(astr),2):
        left = ""
        right = ""
        left = astr[i]
        right = astr[i+1]
        resTmp += left + right + " "
    resTmp = resTmp[:-1]
    resList = resTmp.split()
    resTmp = ""

    for i in resList:
        rowL, columnL = find_letter(i[0])
        rowR, columnR = find_letter(i[1])

        # Row Case
        if rowL == rowR:
            newColL = columnL-1
            if newColL < 0:
                newColL = len(CIPHER[rowL])-1
            newColR = columnR-1
            if newColR < 0:
                newColR = len(CIPHER[rowR])-1
            resTmp += (CIPHER[rowL])[newColL] + CIPHER[rowR][newColR]

        # Rectangle Case
        if rowL != rowR and columnL != columnR:
            newColL = columnR
            newColR = columnL
            resTmp += (CIPHER[rowL])[newColL] + CIPHER[rowR][newColR]

        # Column Case

        if columnL == columnR:
            newRowL = rowL-1
            if newRowL < 0:
                newRowL = len(CIPHER[columnL])-1
            newRowR = rowR-1
            if newRowR < 0:
                newRowR = len(CIPHER[columnR])-1
            resTmp += (CIPHER[newRowL])[columnL] + CIPHER[newRowR][columnR]
    res = resTmp
    return res
