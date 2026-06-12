n1=int(input("Enter size:"))
set1=set()
for i in range(n1):
    set1.add(int(input("Enter elements:")))
print("Set1 is:", set1)

n2=int(input("Enter size:"))
set2=set()
for i in range(n2):
    set2.add(int(input("Enter elements:")))
print("Set2 is:", set2)

print("Union:", set1 | set2)
print("Intersection:", set1 & set2)
print("Difference:", set1 - set2)
print("Symmetric differnce:", set1 ^ set2)
