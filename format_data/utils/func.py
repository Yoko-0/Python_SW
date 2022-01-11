import configparser, os, sys

def get_config():
    config = configparser.ConfigParser()
    path = 'src'
    if not os.path.exists(path):
        path = '../' + path

    for filename in os.listdir(path):
        if filename.endswith('.ini'):
            config.read(f'{path}/{filename}', encoding = 'UTF8')

    return config
