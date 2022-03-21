def clean_dict_value(d, bad_val):
    return {k:v for k,v in d.items() if v !=bad_val}
dirty_dict={'a': 5, 'b': 6, 'c': 5}
print (clean_dict_value(dirty_dict, 6))