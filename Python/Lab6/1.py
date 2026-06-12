n=int(input("Enter size:"))
lst=[]
for i in range(n):
    lst.append(int(input("Enter element:")))
print(lst)
tup=tuple(lst)
print("Reversed tuple is:", tup[::-1])
