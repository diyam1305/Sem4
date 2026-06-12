def SI(P, R, T):
    return (P*R*T)/100
P=int(input("Enter principle:"))
R=float(input("Enter rate:"))
T=int(input("Enter time:"))
print("Simple interest is:", SI(P, R, T))
