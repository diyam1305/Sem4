n=int(input("Enter size:"))
total=0
lst=[]
for i in range(n):
    lst.append(int(input("Enter element:")))
lst[0], lst[-1]=lst[-1], lst[0]
print("Updated list is:")
for ele in lst:
    print(ele)
