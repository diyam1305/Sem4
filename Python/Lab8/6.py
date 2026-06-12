n=int(input("Enter size:"))
dic={}
for i in range(n):
    key=int(input("Enter key:"))
    value=int(input("Enter value:"))
    dic[key]=value
print("Created dictionary is:", dic)
key=int(input("Enter key:"))
if key in dic:
    dic.pop(key)
    print("Updated dictionary is:", dic)
else:
    print("Key not found")
