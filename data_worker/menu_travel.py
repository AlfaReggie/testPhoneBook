from .command import Commands
from .checking import Checking
from .phoneBook import Book
from .contact import Contact

class Travel:

    def __init__(self, PATH_NAME, commands_list: list, question_list: list):
        self.path = PATH_NAME
        self.commands_list = commands_list
        self.quest_list = question_list


    def menu_dir(self):
        self.book_list = Book()
        self.book_list.get_contacts(self.path)
        print(self.book_list)
        commands = Commands(self.commands_list[0])
        print(commands)
        checking = Checking(self.quest_list)
        answ = False
        while answ == False:
            answ = commands.check_command(checking.check_int(5))
        if answ == 1:
            self.menu_lib()

    def menu_lib(self):
        print(self.book_list)
        commands = Commands(self.commands_list[1])
        print(commands)
        checking = Checking(self.quest_list)
        answ = False
        while answ == False:
            answ = commands.check_command(checking.check_int(5))
        if answ == 1:
            if len(self.book_list.contact_list) != 0:
                self.menu_update(False)
            else:
                self.menu_update(True)


    def menu_update(self, empty: bool):
        if empty == False:
            print(self.book_list)
            commands = Commands(self.commands_list[3])
        else:
            commands = Commands(self.commands_list[2])
        print(commands)
        checking = Checking(self.quest_list)
        answ = False
        while answ == False:
            answ = commands.check_command(checking.check_int(5))
        if answ == 1:
            contact = Contact('test', 'test', 'test')
            update_cont = f"\ntest,test,test"
            self.book_list.add_contact(contact)
            self.book_list.update_book(update_cont, self.path)
        if answ == 3:
            checking = Checking(self.quest_list)
            answ = commands.check_command(checking.check_int(6))
            self.book_list.remove_contact(self.book_list.contact_list[answ - 1])
            self.book_list.update_book(self.book_list.contact_list, self.path)

