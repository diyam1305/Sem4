f=open("newfile.txt", "w")
n=int(input("Enter n:"))
for i in range(n):
    f.write(input("Enter data:")+"\n")
f.close()
