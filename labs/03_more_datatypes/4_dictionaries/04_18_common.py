'''
Write a script that takes the following two dictionaries and creates a new dictionary by combining
the common keys and adding the values of duplicate keys together. For example:

_dict1 = {"a": 1, "b": 2, "c": 3}
_dict2 = {"a": 2, "c": 4 , "d": 2}

result = {"a": 3, "b": 2, "c": 7 , "d": 2}


'''

dict1 = {"a": 1, "b": 2, "c": 3}
dict2 = {"a": 2, "c": 4, "d": 2}

result = {key: dict1.get(key, 0) + dict2.get(key, 0)
          for key in set(dict1) | set(dict2)}

print(result)

