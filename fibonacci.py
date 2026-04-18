def fibonnaci(n):
    fib = n
    while n != 1:
        n -= 1
        fib = fib*n
    return fib