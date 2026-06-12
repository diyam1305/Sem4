str1=input("enter string:")
word=str1.split(" ")
for w in word[::-1]:
    print(w,end=" ")
