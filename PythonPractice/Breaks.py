
avail = 5
x = int(input("Enter Number:\n"))
i = 1
while i<=x:
    if i > avail :
        print("Not available")
        break
    print(f"{i}")
    i += 1
