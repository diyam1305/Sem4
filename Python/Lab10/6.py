f=open("studetails.txt", "w")
for i in range(5):
    f.write("Roll No:"+input("Enter Roll No:")+"\n")
    f.write("Name:"+input("Enter Name:")+"\n")
    f.write("Department:"+input("Enter Department:")+"\n")
    f.write("-------------------\n")
f.close()
