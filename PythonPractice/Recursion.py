def factorial(n):
    if n<0:
        return "Factorial not possible"
    if n==1 or n==0:
        return 1
    else:
        return n*factorial(n-1)
print(factorial(7))