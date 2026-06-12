n=int(input("Enter size:"))
dic={}
for i in range(n):
    key=int(input("Enter key:"))
    value=int(input("Enter value:"))
    dic[key]=value
print("Created dictionary is:",dic)
keys=list(dic.keys())
keys.sort()
dic_asc={}
dic_des={}
for i in keys:
    dic_asc[i]=dic[i]
print("Dictionary in ascending is:",dic_asc)
keys.sort(reverse=True)
for i in keys:
    dic_des[i]=dic[i]
print("Dictionary in descending is:",dic_des)
