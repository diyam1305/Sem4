ans=lambda a, b, op : a+b if(op=='+') else a-b if(op=='-') else a*b if(op=='*') else a/b if(op=='/') else a%b if(op=='%') else "Invlid operator"
a=int(input("Enter a:"))
b=int(input("Enter b:"))
op=input("Enter operator:")
print("Ans is:", ans(a, b, op))
