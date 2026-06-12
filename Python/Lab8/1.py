n=int(input("Enter size:"))
dic={}
for i in range(n):
    key=int(input("Enter key:"))
    value=int(input("Enter value:"))
    dic[key]=value
print("Created dictionary is:",dic)
print("Length is:", len(dic))
