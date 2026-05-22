n1=int(input("Enter 1st number:"))
n2=int(input("Enter 2nd number:"))
for i in range(n1, n2):
    for j in range(2, i):
        if i%j==0:
            if i!=j:
               break
    else:
        print(i)
