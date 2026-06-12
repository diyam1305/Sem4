str1=input("enter string:")
count=0
word=str1.split(" ")
for i in word:
    if len(i)%2==0:
        print(i)
        count=count+1
print("No. of even length words:", count)
