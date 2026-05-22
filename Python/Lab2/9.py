unit = int(input("Enter unit:"))
if unit>1 and unit<=50:
    print(unit*2)
elif unit>50 and unit<=100:
    print(unit*3.5)
elif unit>100 and unit<=200:
    print(unit*5.5)
elif unit>200:
    print(unit*2*3.5*5.5*8)
