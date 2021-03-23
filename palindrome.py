def is_palindrome(astr):
    res = ""
    for c in astr:
        if ord(c) >= 97 and ord(c) <= 122:
            res += c
        elif ord(c) >= 65 and ord(c) <= 90:
            res += c
    res = res.upper()
    #print(res[len(res)-1::-1])
    if res == res[len(res)-1::-1]:
        return True
    return False

def create_palindrome(astr):
    if not is_palindrome(astr):
        return astr + astr[len(astr)-1::-1]
    else:
        return astr
