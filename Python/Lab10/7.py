f=open("firstfile.txt", "r")
lst=" ".join(f.read().split("\n")).split()
lword=" "
for i in lst:
    if(len(lword)<len(i)):
        lword=i
print("Largest word is:", lword)
f.close()
