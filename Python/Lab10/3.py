f=open("firstfile.txt", "r")
for i in f.read():
    if not(i.isalnum() or i.isspace()):
        print(i)
f.close()
