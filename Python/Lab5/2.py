n=int(input("Enter size:"))
total=0
lst=[]
for i in range(n):
    lst.append(int(input("Enter element:")))
    if i==0:
        grt=lst[0]
        sml=lst[0]
    if grt<lst[i]:
        grt=lst[i]
    if sml>lst[i]:
        sml=lst[i]
print("Maximum number is:", grt)
print("Minimum number is:", sml)
