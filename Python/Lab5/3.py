n=int(input("Enter size:"))
total=0
lst=[]
for i in range(n):
    lst.append(input("Enter element:"))
mid=len(lst)//2
lst1=lst[:mid]
lst2=lst[mid:]
lst2.extend(lst1)
print(lst2)
