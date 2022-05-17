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


if __name__ == '__main__':
    myBook = AddressBook()
    print(
        'Enter\n 1. To Add Contacts\n 2. To Exit')
    while True:
        choice = int(input('Enter your choice: '))
        if choice == 1:
            myBook.add_contacts()
        elif choice == 2:
            exit()
        else:
            print('Invalid Option. Try Again!')
