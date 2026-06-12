n=int(input("Enter size:"))
total=0
lst=[]
for i in range(n):
    lst.append(int(input("Enter element:")))
lst.reverse()
print("Updated list is:")
for ele in lst:
    print(ele)
