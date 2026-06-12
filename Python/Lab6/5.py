n=int(input("Enter number of tuples:"))
l=[]
for i in range(n):
    n1=int(input("Enter size for tuple:"))
    s1=[]
    for j in range(n1):
        s1.append(int(input("Enter elements:")))
    l.append(tuple(s1))
k=int(input("Enter value of k:"))
for i in l:
    for j in i:
        if j%k==0:
            break
        else:
            print(i)
