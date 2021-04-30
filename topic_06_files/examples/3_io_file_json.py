import json

print('\n--------------------------------------- Write file ----------------------------------------------------------')
dict_to_dump = {"member #002": {"first name": "John", "last name": "Doe", "age": 34},
                "member #003": {"first name": "Elijah", "last name": "Baley", "age": 27},
                "member #001": {"first name": "Jane", "last name": "Doe", "age": 42}}

list_to_dump = [3, 3, [5, 6, 7]]    # тоже можно
tuple_to_dump = (3, 6, 7)    # преобразует в list
set_to_dump = {8, 0, 7}    # TypeError: Object of type set is not JSON serializable

with open('data.json', 'w') as fp:
    # записать
    # ensure_ascii=False если нужен русский язык
    json.dump(dict_to_dump, fp, indent=4, sort_keys=True, ensure_ascii=False)

print('\n--------------------------------------- Read file -----------------------------------------------------------')
with open('data.json') as f:
    loaded_dict = json.load(f)  # прочитать
    print(loaded_dict)
    print(type(loaded_dict), loaded_dict)
