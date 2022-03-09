numbers=[]
while True:
    number=input("Enter number:(q to exit)")
    if number=='q':
        if len(numbers)<6:
            print("Please more..")
            continue
        break
    else:
        numbers.append(float(number))

print(f"{numbers[:3]}...{numbers[-3:]} average:{sum(numbers)/len(numbers)}")