def fib(n):
    if n == 1 or n == 2:
        return 1

    else:
        return fib(n - 1) + fib(n - 2)

def fib3(n):
    if n == 1 or n == 2 or n == 3:
        return 1
    else:
        return fib3(n - 1) + fib3(n - 2) + fib3(n - 3)

def fib_mult(n):
    if n == 1:
        return 1
    if n == 2:
        return 2

    else:
        return fib_mult(n - 1) * fib_mult(n - 2)

def fib_skip(n):
    if n == 1 or n == 2 or n == 3:
        return 1
    else:
        return fib_skip(n - 1) + fib_skip(n - 3)

def joynernacci(n):
    if n == 1 or n == 2:
        return 1

    else:
        if n % 2 ==0:
            return joynernacci(n - 1) + joynernacci(n - 2)
        else:
            return abs(joynernacci(n - 1) - joynernacci(n - 2))
            
