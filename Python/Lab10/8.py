f=open("firstfile.txt", "r")
f.seek(0, 2)
print(f.tell(), "bytes")
f.close()
