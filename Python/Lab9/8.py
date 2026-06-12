n=int(input("Enter n:"))
def prime_no(n):
    for i in range(2, n):
        if n%i==0:
            return 1
            break
    else:
        return 0
prime_no(n)
