import random as r
n=int(input("Enter n:"))
l1=[]
for i in range(n):
    l1.append(input("Enter elements:"))
print("List is:", l1)
print("Random character:", r.choice(l1))
