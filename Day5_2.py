import string
text=input("Enter a text:" )
hidden="*"*len(text)
print(hidden)
guess=input("Enter a symbol:" )
new_hidden=""
for s in text:
    if s==guess:
        new_hidden+=s
    else:
        new_hidden += '*'
print (new_hidden)

