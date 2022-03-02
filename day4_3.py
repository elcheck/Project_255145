n=int(input("number:"))
flag=True
for i in range(2,n):
    if n%i==0:
        flag=False
        break
if flag:
    print(str(n) +" is prime")
else:
    print(str(n)+" is not prime")