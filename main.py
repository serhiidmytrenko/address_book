# coding: utf-8
import pickle

address_book = {}  # This is my Address Book


def create_contact(address_book, name, phone):
    """
    Add curent name
    >>> name('Bob')
    True
    >>> name('jack')
    True
    >>> name('123')
    False
    """
    if not name or not name.isalpha():
        raise ValueError("It's not name, try one more")
    if not phone or not phone.isdigit():
        raise ValueError("It's not phone, try one more")
    address_book[name.capitalize()] = phone




def read_contact():
    #if
    pass


def update_contact():
    pass


def delete_contact():
    pass


while True:
    print (
        """1 - Create
2 - Read
3 - Update
4 - Delete""")
    action = raw_input("What is your choice? ")
    if action and action in 'qQ':
        break
    elif action == '1':
        name = raw_input('Enter the name:   ')
        phone = raw_input('Enter the phone number:  ')
        try:
            create_contact(address_book, name, phone)
        except ValueError as error:
            print error
            print('Try again')
            continue
        print address_book
        contacts = open("contacts_file.txt", 'a')
        pickle.dump(address_book, contacts)
        contacts.close()


    elif action == '2':
        find_contact = raw_input('Enter the name of contact')
        read_contact()
        break
    elif action == '3':
        update_contact()
        break
    elif action == '4':
        delete_contact()
        break
    else:
        print('No such variant, please, choise currect number')
        continue
