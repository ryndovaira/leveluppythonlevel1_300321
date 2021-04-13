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
