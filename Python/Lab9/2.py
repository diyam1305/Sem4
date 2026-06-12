def add(n):
    total=0
    for i in range(n+1):
        total=total+i
    return total
n=int(input("Enter n:"))
print("Total is:", add(n))
