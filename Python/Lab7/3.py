n=int(input("Enter size:"))
set1=set()
for i in range(n):
    set1.add(int(input("Enter elements:")))
print(set1)
n1=int(input("Enter element to be removed:"))
if n1 in set1:
    set1.remove(n1)
    print("Updated set is:", set1)
else:
    print("Element does not exist")
