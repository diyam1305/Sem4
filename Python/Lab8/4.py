n=int(input("Enter size:"))
dic={}
for i in range(n):
    key=int(input("Enter key:"))
    value=int(input("Enter value:"))
    dic[key]=value
print("Created dictionary is:", dic)
key=int(input("Enter key:"))
if key not in dic:
    value=int(input("Enter value:"))
    dic[key]=value
    print(dic)
else:
 print("Key already exist")
