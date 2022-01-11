import configparser, os, sys

def get_config():
    config = configparser.ConfigParser()

    for filename in os.listdir(f'../src'):
        if filename.endswith('.ini'):
            config.read(f'../src/{filename}', encoding = 'UTF8')

    return config
