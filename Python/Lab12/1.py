 class Student:
    def __init__(self, en_rno, name, gender, dept):
        self.rno=en_rno
        self.name=name
        self.gender=gender
        self.department=dept
r=int(input("Enter Enrollment No.:"))
n=input("Enter Name:")
g=input("Enter Gender:")
d=input("Enter Department:")
s=Student(r,n,g,d)
print("Enrollment No.:", s.rno)
print("Name:", s.name)
print("Gender:", s.gender)
print("Department:", s.department)
