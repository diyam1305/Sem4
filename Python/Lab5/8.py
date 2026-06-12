n=int(input("Enter size:"))
total=0
lst=[]
for i in range(n):
    lst.append(int(input("Enter element:")))
lst.sort()
print("Sort list is:")
for i in lst:
    print(i)
