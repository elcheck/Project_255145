n1=float(input("number 1 "))
n2=float(input("number 2 "))
n3=float(input("number 1 "))
ordered_list=''
if n1<n2<n3:
    order_list=str(n1)
    if n2<n3:
        order_list=order_list+", "+ str(n2) + ", " + str(n3)
    else:
        order_list = order_list + ", " + str(n3) + ", " + str(n2)
elif n2 < n1 < n3:
    order_list = str(n2)
    if n1<n3:
        order_list=order_list+", "+ str(n1) + str(n3)
    else:
        order_list = order_list + ", " + str(n3) + ", " + str(n1)
else:
    order_list = str(n3)
    if n1<n2:
        order_list=order_list+", "+ str(n1) + ", "+ str(n2)
    else:
        order_list = order_list + ", " + str(n2) + ", " + str(n1)
print(order_list)