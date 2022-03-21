def replace_dict_value(d,bad_val,good_val):
    for key, value in d.items():
        if value == bad_val:
            d[key]=good_val
    return d
dirty_dict={'a': 5, 'b': 6, 'c': 5}
print(f"incorrect dictionary - {dirty_dict}")
print(f"updated dictionary - {replace_dict_value(dirty_dict,5,10)}")

