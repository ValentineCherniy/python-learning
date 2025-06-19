def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)  # <-- replace this with the recursive call


print(factorial(6))  # this should print 720