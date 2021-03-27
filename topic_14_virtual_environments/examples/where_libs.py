print('\n--------------------------------------- Системные пакеты ----------------------------------------------------')
import sys

print(sys.prefix)  # /usr

print('\n--------------------------------------- Сторонние пакеты ----------------------------------------------------')

import site

data = site.getsitepackages()
print(data)
# ['/usr/local/lib/python3.7/dist-packages', '/usr/lib/python3/dist-packages', '/usr/lib/python3.7/dist-packages']
