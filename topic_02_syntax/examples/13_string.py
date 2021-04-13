print("hello\n\nmy\t\ttab")

empty_str = ""

mul_lines_str = """Привет
это вторая строка
это третья строка
"""

val = 'kdkdj \' djdj " /djdj'
spec_str = "дщдщ \\ ноно \t jkdjfk \" jdjdj ' fff"
print(spec_str)

for i in range(1, 9):
    my_str = "*" * i
    print(f"{my_str}\t!")

string = "Hello"
print('string[0:-1]:', string[0:-1])
print('string[0:0]:', string[0:0])
print('string[0:99]:', string[0:99])
print('string[99:100]:', string[99:100])

print(string[4])
# print(string[99])   # будет ошибка, так как нет символа под номер 100

# ------------------------------

my_long_text = """
Привет
это очень сложный
текст
имеет много слов
Конец!
"""

my_words = my_long_text.split()
print(my_words)
print(my_words[3])
print(my_words[3:26:2])

# -------------------------------------------

my_new_str = "1234567890111"

s1 = my_new_str.replace('7', '!')
print(f"s1: {s1}")

s2 = my_new_str.replace('678', "&")
print(f"s2: {s2}")

s3 = my_new_str.replace('1', "$", 3)
print(f"s3: {s3}")

s4 = (my_new_str[::-1].replace('1', "$", 3))[::-1]
print(f"s3: {s4}")

my_new_str = my_new_str.replace('0', '?')
print(f"my_new_str: {my_new_str}")

# --------------------------------------


my_str_text = "привет я текст! Я Проверяю Методы Строки."
print(my_str_text.upper())
print(my_str_text.lower())
print(my_str_text.capitalize())     # первое слово с большой буквы
print(my_str_text.title())      # каждое слово с большой буквы

# -----------------------------------

print(my_str_text.find('текст'))
print(my_str_text.find('ве'))
print(my_str_text.rfind('ве'))      # r значит, что ищет справа налево
print(my_str_text.find('hello'))    # -1 значит такой подстроки нет
print(my_str_text.find('текстом'))    # -1 значит такой подстроки нет
