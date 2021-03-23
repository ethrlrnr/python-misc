
def find_gcf(nbr1, nbr2):
    if nbr1 >= nbr2:
        if nbr1 % nbr2 == 0:
            return nbr2
    if nbr2 >= nbr1:
        if nbr2 % nbr1 == 0:
            return nbr1
    #Use the Euclidean Algorithm until y equals zero
    while nbr2 > 0:
        nbr1, nbr2 = nbr2, abs(nbr1 - nbr2)
    return nbr1
