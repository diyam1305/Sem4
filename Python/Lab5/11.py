n=int(input("Enter size:"))
total=0
lst=[]
for i in range(n):
    lst.append(int(input("Enter element:")))
print("Odd numbers are:")
for ele in lst:
    if ele%2!=0:
        print(ele, end=" ")
