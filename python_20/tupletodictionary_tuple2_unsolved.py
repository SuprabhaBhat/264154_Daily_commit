#Write a Python program to convert a list of tuples into a dictionary

def Convert(tup, di):
    di = dict(tup)
    return di


# Driver Code
tups = [("suprabha", 10), ("nagaraj", 12), ("arjun", 14),
        ("dhanya", 20), ("aadhya", 25), ("prajwal", 30)]
dictionary = {}
print(Convert(tups, dictionary))