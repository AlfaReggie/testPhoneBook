from const import PATH_NAME, COMMAND_PROGRAM, LIST_VAL
from data_worker import Travel

def start_menu(exit: bool):
    if exit == True:
        print('Ok! Bye =)')
    print("Start programm...\n")
    travel = Travel(PATH_NAME, COMMAND_PROGRAM, LIST_VAL)
    travel.menu_dir()



    '''
    iteration = 0
    while iteration != len(COMMAND_PROGRAM):
        commands = Commands(COMMAND_PROGRAM[iteration])
        print(commands)
        answ = None
        while answ == None:
            answ = commands.check_command(input("Enter number command: "))
        step = commands.menu_steps(int(answ))
        if iteration < 0:
            print('Ok! Bye =)')
            break
        elif step == 0:
            commands.call_menu()
        iteration += step'''