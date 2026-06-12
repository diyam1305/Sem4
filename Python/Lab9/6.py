n=int(input("Enter n:"))
def fibonacci(n):
    a=0
    b=1
    for i in range(n+1):
        print(a, end=" ")
        temp=a+b
        a=b
        b=temp
    print(temp)
fibonacci(n)
