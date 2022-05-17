import json
import os


class AddressBook(object):
    def __init__(self, name=None, address=None, email=None, phone=None, zip=None):
        self.name = name
        self.address = address
        self.email = email
        self.phone = phone
        self.zip = zip
        self.contacts = {}
        self.filename = 'address_book.json'

    def __str__(self):
        return '[Name: {0} | Address: {1} | Email: {2} | Phone: {3} | Zip: {4}]'.format(self.name, self.address,
                                                                                        self.email,
                                                                                        self.phone, self.zip)

    def __repr__(self):
        return '[Name: {0} | Address: {1} | Email: {2} | Phone: {3} | Zip: {4}]'.format(self.name, self.address,
                                                                                        self.email,
                                                                                        self.phone, self.zip)

    # Adding details provided by the user in our Address Book
    def add_contacts(self):
        try:
            if os.path.exists(self.filename) and os.path.getsize(self.filename) > 0:
                myAddressBook = open(self.filename, 'r')
                data = json.load(myAddressBook)
                myAddressBook.close()
            else:
                myAddressBook = open(self.filename, 'w')
                data = {}

            contact = self.get_details_from_user()
            data[contact['Name']] = contact
            myAddressBook = open(self.filename, 'w')
            json.dump(data, myAddressBook, indent=4)
            myAddressBook.close()
            print('Contact Added Successfully!')
        except:
            print('There was an error! Contact was not added.')
        finally:
            myAddressBook.close()

    # Getting the details from the user to adding the Address Book
    def get_details_from_user(self):
        try:
            self.contacts['Name'] = str(input('Enter Contact\'s Full Name: '))
            self.contacts['Address'] = str(input('Enter Contact\'s Address: '))
            self.contacts['Email'] = str(input('Enter Contact\'s Email Address: '))
            self.contacts['Phone'] = int(input('Enter Contact\'s Phone Number: '))
            self.contacts['Zip'] = int(input('Enter Contacts\'s Zip Code: '))
            return self.contacts
        except KeyboardInterrupt as error:
            raise error

    # To display ALL the contact in our Address Book
    def display_contacts(self):
        if os.path.exists(self.filename) and os.path.getsize(self.filename) > 0:
            myAddressBook = open(self.filename, 'r')
            data = json.load(myAddressBook)
            myAddressBook.close()
            if data:
                for records in data.values():
                    print(records)
            myAddressBook.close()
        else:
            print('No Record in database.')

    # To search for a specific contact in our Address Book
    def search_contacts(self):
        if os.path.exists(self.filename) and os.path.getsize(self.filename) > 0:
            myAddressBook = open(self.filename, 'r')
            data = json.load(myAddressBook)
            myAddressBook.close()
            try:
                contactToSearch = input('Enter the name of the contact to search: ')
                counter = 0
                for contact in data.values():
                    if contactToSearch in contact['Name']:
                        print(data[contact['Name']])
                        counter += 1
                if counter == 0:
                    print('No record found whose name is:', contactToSearch)
            except:
                print('Error occurred!')
        else:
            print('No Record in database.')

    # For modifying contacts
    def modify_contacts(self):
        if os.path.exists(self.filename) and os.path.getsize(self.filename) > 0:
            myAddressBook = open(self.filename, 'r')
            data = json.load(myAddressBook)
            myAddressBook.close()
            try:
                contactToModify = input('Enter the name of the contact to modify (Only enter full name): ')
                # Search for the record to update
                for contact in data.values():
                    if contactToModify == contact['Name']:
                        contact = data[contactToModify]
                        break
                option = int(input('1. To modify name, 2. To modify address, 3. To modify email, 4. To modify phone, '
                                   '5. To modify zip:'))
                if option == 1:
                    contact['Name'] = input('Enter Name to modify: ')
                    del data[contactToModify]
                    data[contact['Name']] = contact
                    print('Successful')
                elif option == 2:
                    contact['Address'] = input('Enter Address to modify: ')
                    del data[contactToModify]
                    data[contactToModify] = contact
                    print('Successful')
                elif option == 3:
                    contact['Email'] = input('Enter Email to modify: ')
                    del data[contactToModify]
                    data[contactToModify] = contact
                    print('Successful')
                elif option == 4:
                    contact['Phone'] = input('Enter Phone to modify: ')
                    del data[contactToModify]
                    data[contactToModify] = contact
                    print('Successful')
                elif option == 5:
                    contact['Zip'] = input('Enter Zip to modify: ')
                    del data[contactToModify]
                    data[contactToModify] = contact
                    print('Successful')
                else:
                    print('Incorrect option selected.')
            except:
                print('Error occurred. No such record found. Try Again!')
            finally:
                myAddressBook = open(self.filename, 'w')
                json.dump(data, myAddressBook, indent=4)
                myAddressBook.close()
        else:
            print('No Record in database.')


if __name__ == '__main__':
    myBook = AddressBook()
    print(
        'Enter\n 1. To Add Contacts\n 2. To Display '
        'Contacts\n 3. For Searching a Contact\n 4. For Modifying a Contact\n 5. To Exit')
    while True:
        choice = int(input('Enter your choice: '))
        if choice == 1:
            myBook.add_contacts()
        elif choice == 2:
            myBook.display_contacts()
        elif choice == 3:
            myBook.search_contacts()
        elif choice == 4:
            myBook.modify_contacts()
        elif choice == 5:
            exit()
        else:
            print('Invalid Option. Try Again!')
