size=int(input("Enter size:"))
lst_tup=[]
for i in range(size):
    s=int(input("Enter size of tuple:"))
    lst=[]
    for j in range(s):
        lst.append(int(input("Enter elements:")))
    lst_tup.append(tuple(lst))
print(lst_tup)
for t in lst_tup:
    for j in t:
        if j<0:
            break
    else:
        print("Tuple with positive elements:", t)
