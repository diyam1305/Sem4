n=int(input("Enter size:"))
lst=[]
for i in range(n):
    lst.append(int(input("Enter key:")))
print("List1:", lst)
n2=int(input("Enter size:"))
lst2=[]
for i in range(n2):
    lst2.append(int(input("Enter value:")))
print("List2:", lst2)
dic={}
for i in range(n):
     dic[lst[i]]=lst2[i]
print("Dictionary:", dic)
