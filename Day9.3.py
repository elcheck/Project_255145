def is_pangram(text, alphabet='abcdefghijklmnopqrstuvwxyz'):
    return(len(tuple(set(alphabet).difference(set(text.lower()))))==0)
text1="Not a pangram"
print(f"text: {text1} -> {is_pangram(text1)}")
text2="The five boxing wizards jump quickly"
print(f"text: {text2} -> {is_pangram(text2)}")