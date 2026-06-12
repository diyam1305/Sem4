n=int(input("Enter size:"))
dic={}
for i in range(n):
    key=int(input("Enter key:"))
    value=int(input("Enter value:"))
    dic[key]=value
print("Created dictionary is:", dic)
values=list(dic.values())
values.sort()
dic_asc={}
dic_des={}
for i in values:
    for j in dic:
        if dic[j]==i:
            dic_asc[j]=i
print("Dictionary in ascending order is:", dic_asc)
values.sort(reverse=True)
for i in values:
    for j in dic:
        if dic[j]==i:
            dic_des[j]=i
print("Dictionary in descending order is:", dic_des)
