def exponent_calc(base, expo):
    if expo == 0:
        return 1
    else:
        return base*exponent_calc(base, expo-1)
