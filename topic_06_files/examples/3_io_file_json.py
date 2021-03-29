import json

print('\n--------------------------------------- Write file ----------------------------------------------------------')
dict_to_dump = {"member #002": {"first name": "John", "last name": "Doe", "age": 34},
                "member #003": {"first name": "Elijah", "last name": "Baley", "age": 27},
                "member #001": {"first name": "Jane", "last name": "Doe", "age": 42}}

with open('data.json', 'w') as fp:
    json.dump(dict_to_dump, fp, indent=4, sort_keys=True)   # ensure_ascii=False если нужен русский язык

print('\n--------------------------------------- Read file -----------------------------------------------------------')
with open('data.json') as f:
    loaded_dict = json.load(f)
    print(loaded_dict)
    print(type(loaded_dict), loaded_dict)
