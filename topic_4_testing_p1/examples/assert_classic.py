passed = False
assert passed, 'Not passed'  # Поднимается исключение.
# assert passed  # Можно и не указывать текст описания, но рекомендуется.


a = 'Long exception '
# Пример правильного переноса строки описания:
assert a, ('Long exception '
           'description chunked.')

# А теперь пример неправильного (передача кортежа),
# при котором проверка всегда проходит без ошибок:
# assert (a, 'Long exception '
#            'description chunked.')
