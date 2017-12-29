import csv

class PhonebookOperations:
    def addname(self, phonebook, name, value):
        phonebook[name] = value
        self.write_file()
        print(phonebook)

    def viewname(self, name, phonebook):
        return phonebook[name]

    def update_name(self, phonebook, name, value):
        phonebook[name] = value

    def delete_name(self, phonebook, name):
        del phonebook[name]

class Serialize:
    def write_file(self, phonebook):
        try:
            with open('names.csv', 'w', newline='') as csvfile:
                writer = csv.writer(csvfile, delimiter=',', quotechar='"', quoting=csv.QUOTE_ALL)

                for row in phonebook.items():
                    writer.writerow(row)

                csvfile.close()
        except IOError:
            print("I/O error({0}): {1}")

    def read_file(self):
        try:
            with open('names.csv', 'r', newline='') as csvfile:
                spamreader = csv.reader(csvfile)
                phonebook = {name: phone for name, phone in spamreader}
                csvfile.close()
        except IOError:
            print("I/O error({0}): {1}")

        return phonebook

#some = Serialize()
#phonebook = some.read_file()

#phonebook['mole'] = '123123'
#print(phonebook)

#some.write_file(phonebook)


