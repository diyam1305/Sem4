n=int(input("Enter size:"))
lst=[]
for i in range(n):
    lst.append(int(input("Enter element:")))
print(lst)
lst2=[]
tup=tuple(lst)
for i in tup:
    if i not in lst2:
        lst2.append(i)
tup2=tuple(lst2)
if len(tup)==len(tup2):
    print("Distinct")
else:
    print("Not distinct")
