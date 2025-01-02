import math as m

def prime(n):
    if n <= 1:
        return False
    for i in range (2, int(m.sqrt(n)+1)):
        if n % i == 0:
            return False
    return True

num = int(input("Enter number to check\n"))
if prime(num):
    print(f"{num} is Prime")
else:
    print(f"{num} is Not Prime")



