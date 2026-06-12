n=int(input("Enter size:"))
set1=set()
for i in range(n):
    set1.add(int(input("Enter elements:")))
print("Set is:",set1)
tup=tuple(set1)
print("Tuple is:", tup)
lst=list(set1)
print("List is:", lst)
