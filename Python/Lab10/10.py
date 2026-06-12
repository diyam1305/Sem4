import os
path=input("Enter file path:")
if os.path.exists(path):
    confirm=input("Do u want to delete this file or not(YES/NO):")
    if confirm=="yes":
        os.remove(path)
else:
    print("File does not exist")
