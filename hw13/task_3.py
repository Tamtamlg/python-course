import os
import configparser

CONFIG_FILE = 'hero.ini'
SECTION_NAME = 'Hero'

path = os.path.dirname(os.path.realpath(__file__))
config = configparser.ConfigParser()
config.read(os.path.join(path, CONFIG_FILE))


def update_hero(**kwargs):
    for key, value in dict(**kwargs).items():
        config.set(SECTION_NAME, str(key), str(value))
    with open(os.path.join(path, CONFIG_FILE), 'w') as file:
        config.write(file)


if __name__ == '__main__':
    update_hero(hero="Halk", power=450, Y=2.3)
