def rec_fibonacci(n):
    if n<=1:
        return n
    else:
        return rec_fibonacci(n-1) + rec_fibonacci(n-2)
n=int(input("Enter n:"))
print("Fibonacci series:")
for i in range(n):
    print(rec_fibonacci(i), end=" ")
