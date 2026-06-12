def recursion_fact(n):
    if n==1:
        return n
    else:
        return n * recursion_fact(n-1)
n=int(input("Enter n:"))
print("Factorial is:", recursion_fact(n))
