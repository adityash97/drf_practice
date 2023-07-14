def remove_none_from_dict(dict):
    for k in dict:
        if dict[k] == None:
            del dict[k]
    return dict