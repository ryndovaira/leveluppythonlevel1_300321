word_1 = input('1 слово: ')
word_2 = input('2 слово: ')
word_3 = input('3 слово: ')

print(word_1, word_2, word_3)
print(word_1, word_2, word_3, sep='-')
print(word_1, word_2, word_3, sep='***')
print(word_1, word_2, word_3, sep='ooo')
print(word_1, word_2, word_3, sep='')

print('-----------------------------------------------------------------------------')
# Если нужно много одинаковых разделителей
print(word_1, word_2, word_1, word_2, word_1, word_2, word_1, sep='*', end='')
print('-', word_3, sep='')

# Если все хорошо выглядит в одну строку
print(word_1, '*', word_2, '-', word_3, sep='')

print('-----------------------------------------------------------------------------')

my_sep = input('sep: ')
print(word_1, word_2, word_3, sep=my_sep)
