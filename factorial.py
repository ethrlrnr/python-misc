def factorial(n):
    #What do we want to do inside the function? Well, there
    #are two cases. First, if n is 1, we just want to return
    #1. After all, 1! is 1.

    if n == 1:
        return 1

    #What if n doesn't equal 1, though? Then we want to
    #return n times the factorial of (n - 1). After all,
    #5! = 5 * 4!, 4! = 4 * 3!, etc.

    else:
        return n * factorial(n - 1)
