
ini_tuple = [('b', 100), ('c', 200), ('c', 45),
             ('d', 876), ('e', 75)]

print("intial_list", str(ini_tuple))

# removing tuples for condition met
result = [i for i in ini_tuple if i[1] <= 100]

# printing resultant tuple list
print("Resultant tuple list: ", str(result))

