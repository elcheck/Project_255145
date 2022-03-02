FizzBuzz=""
for i in range(1,101):
    if i%5==0:
        FizzBuzz+="Fizz"
    if i%7==0:
        FizzBuzz+="Buzz"
    if not (i%5==0 or i%7==0):
        FizzBuzz+=str(i)
    if i!=100:
        FizzBuzz+=","
print(FizzBuzz)
