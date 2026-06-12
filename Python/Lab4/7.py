str1=input("enter string:")
d=int(input("enter value of d(no. of rotates):"))
left_result=str1[d:]+str1[:d]
print("New string after left rotate:", left_result)
str1=input("enter string:")
right_result=str1[-d:]+str1[:-d]
print("New string after right rotate:", right_result)
