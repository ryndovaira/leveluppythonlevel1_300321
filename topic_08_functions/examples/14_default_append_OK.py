def append_default(element, lst=None):
    if lst is None:
        lst = []

    lst.append(element)
    return lst


print(append_default("1"))  # ['1']

print(append_default("2"))  # ['2']

# ---------------------------------------

my_list = []

print(append_default(3, my_list))   # [3]

print(append_default(4, my_list))   # [3, 4]

print(my_list)      # [3, 4]
