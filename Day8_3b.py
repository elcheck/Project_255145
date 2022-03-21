def clean_dict_value(d, v_list):
    return {k:v for k,v in d.items() if v not in v_list}
dirty_dict={'a': 5, 'b': 6, 'c': 5, 'd':3}
print (clean_dict_value(dirty_dict, [3,4,5]))