import string
name=input('Enter a name: ')
extra='a thorough mess is it not '
name_reverse=name[::-1]
print(f"{name_reverse.title()}, {extra} {name[0]}")