def fib(i):
    if i <= 2:
        return 1;
    else:
        f = fib(i-1) + fib(i-2)
    return f