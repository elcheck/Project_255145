numbers=[]
while True:
    number=input("Enter number:(q to exit)")
    if number=='q':
        if i<6:
            print("Please more..")
            continue
        break
    else:
        numbers.append(float(number))
        i+=1
        sum+=float(number)
print(f"{numbers[:3]}...{numbers[-3:]} average:{sum/i}")