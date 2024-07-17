my_dict = {'a': 1, 'b': 2, 'c': 3 ,'d':4}

# Using get method
print(my_dict.get('b'))   #Output: 4

# Using items method
print(my_dict.items())    #Output: dict_items([('a', 1), ('b', 2), ('c', 3), ('d', 4)])

#Using keys method
print(my_dict.keys())    #Output: dict_keys(['a', 'b', 'c', 'd'])

# Using values method
print(my_dict.values())  #Output: dict_values([1, 2, 3, 4])

# Using update method
my_dict.update({'d': 4})
print(my_dict)  #Output: {'a': 1, 'b': 2, 'c': 3, 'd': 4}

# Using pop method
value = my_dict.pop('a')
print(value)    # Output: 1
print(my_dict)  # Output: {'b': 2, 'c': 3, 'd': 4}

# Using popitem method
key, value = my_dict.popitem()
print(key, value)  #Output: 'd' 4
print(my_dict)     #Output: {'b': 2, 'c': 3}
