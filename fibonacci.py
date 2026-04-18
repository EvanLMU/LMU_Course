def fibonnaci(n):
    fib = n
    while n != 1:
        n -= 1
        fib = fib*n
    print("The fibonnaci value of " + str(n) + " is " + str(fib))
    return None

def count(n):
    for i in range(n):
        print(n)

count(5)
fibonnaci(5)