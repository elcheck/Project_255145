import string
name=input('Enter a name: ')
extra='a thorough mess is it not '
name_reverse=name[::-1].capitalize()
print(f"{name_reverse}, {extra} {name[0]}")