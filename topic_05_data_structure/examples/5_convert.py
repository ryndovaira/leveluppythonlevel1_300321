print('\n--------------------------------------- Common --------------------------------------------------------------')

# list -> tuple
list_numbers = [6, 3, 7, 4]
x = tuple(list_numbers)
print(x)  # (6, 3, 7, 4)

# tuple -> list
x = (4, 5)
list_numbers = list(x)
print(list_numbers)  # [4, 5]

# tuple -> string
person = ('Diana', 'Canada', 'CompSci')
s = '-'.join(person)
print(s)  # Diana-Canada-CompSci

# list -> string
# только, если все элементы list являются str
list_count = ['one', 'two', 'many']
s = ', '.join(list_count)
print(s)  # one, two, many

# list -> string
list_misc = ["a", "sample", 44, 55, "program"]
s = '_'.join([str(elem) for elem in list_misc])
print(s)  # a_sample_44_55_program

l_str = str(list_misc)
print(l_str)

print('\n--------------------------------------- Eval ----------------------------------------------------------------')
list_str = '[1, 4, 6, "fff", True]'
converted_list = eval(list_str)
print(f'type({list_str}) = {type(list_str)} | type({converted_list}) = {type(converted_list)}')

tuple_str = '(1, 4, 6, "fff", True)'
converted_tuple = eval(tuple_str)
print(f'type({tuple_str}) = {type(tuple_str)} | type({converted_tuple}) = {type(converted_tuple)}')

set_str = '{1, 4, 6, "fff", True}'
converted_set = eval(set_str)
print(f'type({set_str}) = {type(set_str)} | type({converted_set}) = {type(converted_set)}')

dict_str = '{1: "ttt", 4: "rrr", 6: False, "fff": True, True: 111}'
converted_dict = eval(dict_str)
print(f'type({dict_str}) = {type(dict_str)} | type({converted_dict}) = {type(converted_dict)}')
