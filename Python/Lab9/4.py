def str_func(str1):
    str2=" "
    for i in str1:
        if i.islower():
            str2+=i.upper()
        else:
            str2+=i
    print(str2)
str1=input("Enter string:")
str_func(str1)
