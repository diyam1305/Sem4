str1=input("enter string:")
count=0
for i in str1:
    if(i=='a' or i=='e' or i=='i' or i=='o' or i=='u' or i=='A' or i=='E' or i=='I' or i=='O' or i=='U'):
        count=count+1
print("Total vowels:", count)
