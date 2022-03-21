def get_char_count(text):
    letter_count_dict={}
    for c in text.replace(' ','').lower():
        if c in letter_count_dict.keys():
            letter_count_dict[c]+=1
        else:
            letter_count_dict[c]=1
    return letter_count_dict
print(get_char_count('hubBa bubBa'))