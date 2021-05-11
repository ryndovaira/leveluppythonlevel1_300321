a = 55      # немутабельный int
lst_tmp = [1, 2, 3]     # мутабельный (изменяемый) list


def append_default(element=a, lst=[], lst2=lst_tmp):
    lst.append(element)
    lst2.append(element)    # изменили состояние переменной lst_tmp
    return element, lst, lst2


print(f'append_default() = {append_default()}')  # (55, [55], [1, 2, 3, 55])
print(f'lst_tmp = {lst_tmp}\n')     # [1, 2, 3, 55]

a = 77
lst_tmp.append('a')
print(f'append_default() = {append_default()}')  # (55, [55, 55], [1, 2, 3, 55, 'a', 55])
print(f'lst_tmp = {lst_tmp}\n')     # lst_tmp = [1, 2, 3, 55, 'a', 55]

print(f'append_default() = {append_default()}')  # (55, [55, 55, 55], [1, 2, 3, 55, 'a', 55, 55])
print(f'lst_tmp = {lst_tmp}\n')     # [1, 2, 3, 55, 'a', 55, 55]
