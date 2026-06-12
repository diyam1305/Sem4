n=int(input("Enter size:"))
lst=[]
for i in range(n):
    lst.append(int(input("Enter elements:")))
set1=set(lst)
print("Created set is:", set1)
print("Length of set is:", len(set1))
