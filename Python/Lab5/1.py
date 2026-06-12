n=int(input("Enter size:"))
total=0
lst=[]
for i in range(n):
    lst.append(int(input("Enter element:")))
    total+=lst[i]
print(total)
