n=int(input("Enter size:"))
total=0
lst=[]
for i in range(n):
    lst.append(int(input("Enter element:")))
lst1=int(input("Enter 1st index:"))
lst2=int(input("Enter 2nd index:"))
lst[lst1], lst[lst2]=lst[lst2], lst[lst1]
print("New list is:")
for ele in lst:
    print(ele)
