def Merge(dict1, dict2):
    return (dict2.update(dict1))

dict1 = {'a': 4, 'b': 2}
dict2 = {'d': 6, 'c': 8}

print(Merge(dict1, dict2))

print(dict2)