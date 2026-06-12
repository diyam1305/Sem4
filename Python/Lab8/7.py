n1=int(input("Enter size:"))
dic1={}
for i in range(n1):
    key=int(input("Enter key:"))
    value=int(input("Enter value:"))
    dic1[key]=value
print("Created dictionary is:", dic1)
n2=int(input("Enter size:"))
dic2={}
for i in range(n2):
    key=int(input("Enter key:"))
    value=int(input("Enter value:"))
    dic2[key]=value
print("Created dictionary is:", dic2)
for i in dic2:
        dic1[i]=dic2[i]
print("Concated dictionary is:", dic1)
