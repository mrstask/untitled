import os.path
import configparser

from files import Serialize

#спросить как правильно записывать словарь в файл

#check if config exists
if os.path.isfile('config.ini'):
    config = configparser.ConfigParser()
    config.read('config.ini')
    file_type = config['Section1']['Type']
else:
    print('No config file')

phonebook = {}




#user
print('if you want to create enter 1')
print('if you want to read enter 2')
print('if you want to update enter 3')
print('if you want to delete enter 4')
print('if you want to quit enter 5')


while True:
    keyboard_input = input('what do you want to do ')
    if keyboard_input == '1':
        name = input('add name ')
        value = input('add num ')
        addname(name, value)

    elif keyboard_input == '2':
        name = input('input name to view ')
        print(Serialize.read_file())

    elif keyboard_input == '3':
        name = input('input name to update ')
        value = input('input new num to update ')
        update_name(name, value)
        print(phonebook)

    elif keyboard_input == '4':
        name = input('input name to delete ')
        delete_name(name)
        print(phonebook)

    elif keyboard_input == '5':
        break