import csv
import json
import os.path
import configparser

#спросить как правильно записывать словарь в файл

#check if config exists
if os.path.isfile('config.ini'):
    config = configparser.ConfigParser()
    config.read('config.ini')
    file_type = config['Section1']['Type']
else:
    print('No config file')

phonebook = {}

def read_file():
    try:
        with open('names.csv', 'r', newline='') as csvfile:
            spamreader = csv.reader(csvfile)
            phonebook = {name: phone for name, phone in spamreader}
            csvfile.close()
    except IOError as (errno, strerror):
            print("I/O error({0}): {1}".format(errno, strerror))

    return phonebook

def write_file():
    try:
        with open('names.csv', 'w', newline='') as csvfile:
            writer = csv.writer(csvfile, delimiter=',', quotechar='"', quoting=csv.QUOTE_ALL)

            for row in phonebook:
                print(row)
                writer.writerow(row)

            csvfile.close()
    except IOError as (errno, strerror):
        print("I/O error({0}): {1}".format(errno, strerror))


print(read_file())
print("__________________________")



#user
print('if you want to create enter 1')
print('if you want to read enter 2')
print('if you want to update enter 3')
print('if you want to delete enter 4')
print('if you want to quit enter 5')



def addname(name, value):
    phonebook[name] = value
    write_file()
    print(phonebook)


def viewname(name, phonebook):
    return phonebook[name]

def update_name(name, value):
    phonebook[name] = value

def delete_name(name):
    del phonebook[name]

while True:
    keyboard_input = input('what do you want to do ')
    if keyboard_input == '1':
        name = input('add name ')
        value = input('add num ')
        addname(name, value)

    elif keyboard_input == '2':
        name = input('input name to view ')
        result = viewname(name)
        print(result)

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