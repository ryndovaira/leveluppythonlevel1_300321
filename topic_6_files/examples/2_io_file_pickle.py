import pickle

print('\n--------------------------------------- Write file (dict) binary --------------------------------------------')
my_dict = {'Python': '.py', 'C++': '.cpp', 'Java': '.java'}
with open("dict.pkl", "wb") as f:
    pickle.dump(my_dict, f)

print('\n--------------------------------------- Write file (list) binary --------------------------------------------')
my_list = ['Python', 'C++', 'Java']
with open("list.pkl", "wb") as f:
    pickle.dump(my_list, f)

print('\n--------------------------------------- Read file (dict) binary ---------------------------------------------')
with open("dict.pkl", 'rb') as f:
    dict_from_file = pickle.load(f)
print(type(dict_from_file), dict_from_file)

print('\n--------------------------------------- Read file (list) binary ---------------------------------------------')
with open("list.pkl", 'rb') as f:
    list_from_file = pickle.load(f)
print(type(list_from_file), list_from_file)
