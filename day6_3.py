text=input("enter sentence:")
words=text.split()
print(words)
reversed_words=[word[::-1] for word in words]
text_reversed=" ".join([word for word in reversed_words])
print(text_reversed.capitalize())