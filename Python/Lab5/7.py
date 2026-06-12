n=int(input("Enter size:"))
total=0
lst=[]
for i in range(n):
    lst.append(int(input("Enter element:")))
s=int(input("Enter value to search:"))
if s in lst:
    print("Element found!")
else:
    print("Element not found!")
