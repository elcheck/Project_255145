#  2. Exercise - Room volume
#
# Ask user to input 3 numbers - width, length, height
# Find the volume of the room
# PS Think about units and what is the most appropriate data type for this
w=float(input("weight (cm)?:"))
l=float(input("length (cm)?:"))
h=float(input("height (cm)?:"))
volume=round(w*l*h/100**3,2)
print(f"Room Volume {volume} m3")
