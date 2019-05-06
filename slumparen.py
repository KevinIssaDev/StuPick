from os import system
from random import choice
from msvcrt import getch
from colorama import init, Fore

init(autoreset=True)
klass = None

class Keys:
    enter = b'\r'
    esc = b'\x1b'
    one = "1".encode()
    two = "2".encode()
    three = "3".encode()
    four = "4".encode()
    five = "5".encode()

def log_crash(error):
    with open("log.txt", "a") as f:
        f.write(str(error))
    print("Något gick fel, en crash-logg har skapats (log.txt). Visa Kevin Issa TE17!")
    print("Du kan starta om programmet eller byta klass (till samma), då bör det funka.")

def cls(all = False, menu = True):
    system('cls')
    items = ["Slumpa en elev", "Slumpa flera elever", "Skapa grupper" ,"Byt klass", "Lägg till klass"]
    if not all:
        print("Klass: " + Fore.YELLOW + klass.upper() + "\n")
    if menu:
        for num, val in enumerate(items, 1):
            print("{} - {}".format(num, val))
        print()

def get_class(merging = False):
    class_name = input("Klass: ")
    class_list = load_class(class_name, merging = merging)
    return class_list

def load_class(class_name, merging = False):
    global klass
    try:
        with open(class_name + ".txt", "r") as class_file:
            class_list = class_file.readlines()
        class_list = ['{} {[0]}'.format(*student.split()) for student in class_list]
        if not merging:
            klass = class_name
        else:
            klass = klass + Fore.RESET + " & " + Fore.GREEN + class_name
        return class_list
    except:
        print(Fore.RED + "Klassen hittades inte, försök igen.")
        class_list = get_class()

def random_student(class_list, multiple=False):
    if multiple:
        amount = get_int_input("Antal: ")
        if amount > len(class_list):
            amount = len(class_list)
        while True:
            picked_students = set()
            cls()
            try:
                for x in range(1, amount+1):
                    unique = False
                    while not unique:
                        picked_student = choice(class_list)
                        if picked_student not in picked_students:
                            unique = True
                        picked_students.add(picked_student)
                    print("Slumpad elev " + str(x) + ": " + Fore.GREEN + picked_student)
            except Exception as e:
                log_crash(e)
                getch()
                return
            press = getch()
            if press != Keys.enter:
                print("not enter")
                break
    else:
        while True:
            cls()
            try:
                print("Slumpad elev: " + Fore.GREEN +choice(class_list))
            except Exception as e:
                log_crash(e)
                getch()
                return
            press = getch()
            if press != Keys.enter:
                break

def divide_chunks(l, n):
    for i in range(0, len(l), n):
        yield l[i:i + n]

def create_groups(class_list):
    size_per_group = get_int_input("Antal elever per grupp: ")
    cls()
    groups = list(divide_chunks(class_list, size_per_group))
    print(Fore.YELLOW + "Grupper: {}\n".format(str(len(groups))))
    for num, group in enumerate(groups, 1):
        print("Grupp {}: ".format(num) + Fore.GREEN + ', '.join(group))
    getch()


def get_int_input(text):
    valid = False
    while not valid:
        _input = input(text)
        try:
            _input = int(_input)
            valid = True
        except:
            print(Fore.RED + "Ogiltigt nummer, försök igen.")
    return _input

def merge_classes(class_list):
    class_list += get_class(merging = True)
    return class_list

def run():
    cls(all = True, menu = False)
    class_list = get_class()
    while True:
        cls()
        option = getch()
        try:
            if option == Keys.one:
                random_student(class_list)
            elif option == Keys.two:
                random_student(class_list, multiple=True)
            elif option == Keys.three:
                create_groups(class_list)
            elif option == Keys.four:
                class_list = get_class()
            elif option == Keys.five:
                merge_classes(class_list)
            elif option == Keys.esc:
                 break
            else:
                pass
        except:
            log_crash()

run()
