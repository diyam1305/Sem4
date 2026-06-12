f=open("studetails.txt", "a")
n=int(input("Enter n:"))
for i in range(n):
    f.write("Roll No:"+input("Enter Roll No:")+"\n")
    f.write("Name:"+input("Enter Name:")+"\n")
    f.write("Department:"+input("Enter Department:")+"\n")
    f.write("-------------------\n")
f.close()
