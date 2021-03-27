from configparser import ConfigParser

config = ConfigParser()

# загрузить конфигурационный файл
config.read("config.ini")

print(f"\nconfig: {config}")
# <configparser.ConfigParser object at 0x7f953effbca0>

# получить доступ к данным по ключу "debug" в разделе "DEFAULT"
get_debug_result = config.get('DEFAULT', 'debug')
print(f"\nget('DEFAULT', 'debug'): {get_debug_result}\n"
      f"type(get('DEFAULT', 'debug')): {type(get_debug_result)}\n")
# True
# <class 'str'>

# получить доступ к данным по ключу  "path" в разделе "FILES"
get_path_result = config.get('FILES', 'path')
print(f"get('FILES', 'path'): {get_path_result}\n"
      f"type(get('FILES', 'path')): {type(get_path_result)}\n")
# ./ex/example.txt
# <class 'str'>

# получить список разделов (все кроме раздела по умолчанию)
print(f"\nsections(): {config.sections()}")
# [['Strange section with spaces', 'FILES', 'bitbucket.org', 'server.com']
# Раздел DEFAULT не будет включен

# получить название раздела по умолчанию
print(f"\ndefault_section: {config.default_section}\n")
# DEFAULT

print(f"'bitbucket.org' in config: {'bitbucket.org' in config}")
# True

print(f"'no_name.org' in config: {'no_name.org' in config}")
# False

print("\nconfig.defaults():")
for key in config.defaults():
    print(f"\t{key}")
# debug
# name
# password

print(config['DEFAULT'].getboolean('debug'))

# получить доступ к данным по ключу "debug" в разделе "DEFAULT"
get_bool_debug_result = config.getboolean('DEFAULT', 'debug')
print(f"\ngetboolean('DEFAULT', 'debug'): {get_bool_debug_result}\n"
      f"type(getboolean('DEFAULT', 'debug')): {type(get_bool_debug_result)}\n")
# True
# <class 'bool'>


# получить доступ к данным по ключу "Port" в разделе "server.com"
get_int_port_result = config.getint('server.com', 'Port')
print(f"\ngetint('server.com', 'Port'): {get_int_port_result}\n"
      f"type(getint('server.com', 'Port')): {type(get_int_port_result)}\n")
# 50022
# <class 'int'>
