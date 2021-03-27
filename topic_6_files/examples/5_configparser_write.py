import configparser

config = configparser.ConfigParser()

config['settings'] = {'resolution': '320x240',
                      'color': 'blue'}
config['misc'] = {'name': 'Ira',
                  'id': 777}

with open('example.ini', 'w') as configfile:
    config.write(configfile)
