#  2. Exercise - Room volume
#
# Ask user to input 3 numbers - width, length, height
# Find the volume of the room
# PS Think about units and what is the most appropriate data type for this
w=int(input("weight (cm)?:"))
l=int(input("length (cm)?:"))
h=int(input("height (cm)?:"))
volume=w*l*h/100**3
print(f"Room Volume {volume} 300m3")
