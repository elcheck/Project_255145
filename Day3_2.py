salary=float(input("Monthly Salary: "))
years=float(input("number of years: "))
if years>2:
    bonus=(years-2)*(salary*15/100)
else:
    bonus=0
print(f"bonus={bonus}")