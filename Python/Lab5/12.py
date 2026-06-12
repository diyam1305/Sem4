lst=[]
for i in range(5):
    name=input("Enter name of product:")
    quantity=int(input("Enter quantity of product:"))
    price=float(input("Enter price of product:"))
    totl_amnt=quantity*price
    lst.append((name, quantity, price, totl_amnt))
print("Product details:")
for pro in lst:
    name, quantity, price, totl_amnt=pro
    print("Name:", name)
    print("Quantity:", quantity)
    print("Price:", price)
    print("Total Amount:", totl_amnt)
