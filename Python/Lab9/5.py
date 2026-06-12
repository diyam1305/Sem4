n=int(input("Enter n:"))
def fact(n):
    fact=1
    print("Factorial is:")
    for i in range(1, n+1):
        fact=fact*i
    print(fact)
fact(n)
