# 3. Exercise - Temperature Conversion
#
# Write a program that asks user for temperature in Celsius and prints out this same temperature in Farenheit
# formula is: farenheit = 32+celsius*(9/5)
# PS Remember about data type conversion, also consider precision
c=float(input("Celsius:"))
f=round(32+c*(9/5),2)
print(f"Farenheit: {f}")
