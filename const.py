import os

PATH_NAME = os.path.join('data', 'Contacts_Book.txt')

COMMAND_START = ['Open phone book', "Stop program"]
COMMAND_LIBR = ["Update file", "Save in CSV", 'Search contact', "Exit to library"]
COMMAND_EMPTY_FILE = ["Add contact", 'Exit to files']
COMMAND_FILE = ["Add contact", "Update contacts", 'Delete contacts', 'Exit to files']
COMMAND_SEARCH = ['Search on first name', 'Search on family name', 'Search on phone', 'Exit to contact menu']

COMMAND_PROGRAM = [COMMAND_START, COMMAND_LIBR, COMMAND_EMPTY_FILE, COMMAND_FILE, COMMAND_SEARCH]

LIST_VAL = ["name", "family name", "phone", "file name", "file number", "command number", "contact number"]
