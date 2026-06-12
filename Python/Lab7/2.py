n=int(input("Enter size:"))
set1=set()
for i in range(n):
    set1.add(int(input("Enter elements:")))
print("Created set is:", set1)
print("Max element:", max(set1))
print("Min element:", min(set1))
