n=int(input("Enter n:"))
sum=0
rem=0
while n>0:
    rem=n%10
    sum=rem+sum
    n=n//10
print(sum)
