def append_default(element, lst=[]):
    lst.append(element)
    return lst


my_result = append_default("1")

print(my_result)  # ['1']

my_result.append("4")

print(my_result)    # ['1', '4']

print(append_default("2"))  # ['1', '4', '2']
