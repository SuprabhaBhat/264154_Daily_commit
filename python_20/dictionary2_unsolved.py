num_list = [6, 8, 3, 5]
new_dict = curr = {}
for name in num_list:
    curr[name] = {}
    curr = curr[name]
print(new_dict)