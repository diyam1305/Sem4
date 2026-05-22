op=input("Enter operator:")
a=int(input("Enter value of a:"))
b=int(input("Enter value of b:"))
if op=='+':
    print("Addition is:", a+b)
elif op=='-':
    print("Subtraction is:", a-b)
elif op=='*':
    print("Multiplication is:", a*b)
elif op=='/':
    print("Divsion is:", a/b)
else:
    print("Enter valid number")
