my_str = 'Hello!'
if '!' in my_str:
    print(f'I found it in {my_str}')

if '???' not in my_str:
    print(f'I did not find it in {my_str}')

if "ddd" in my_str and "!" in my_str:
    print("ldld")

# --------------------------------------------

my_list = ['a', 55, 'bb', True, 'gjgf', 66, False]
my_dict = {'a': 66, 'cc': 'word', 777: 'bingo!', True: 'true'}
my_tuple = (22, 'char', 888, True)
my_set = {22, 'char', 888, True}

if 'bb' in my_list:
    print(f'I found it in {my_list}')

if 777 in my_dict:
    print(f'I found it in {my_dict}')

if True in my_tuple:
    print(f'I found it in {my_tuple}')

if 22 in my_set:
    print(f'I found it in {my_set}')


