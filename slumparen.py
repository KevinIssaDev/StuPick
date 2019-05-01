from os import system
from random import choice
import keyboard

klass = None
menu_list = "[1] - Slumpa elev\n[2] - Byt klass\n[3] - Lägg till klass\n"

def cls(all = False, menu = True):
    system('cls')
    if not all:
        print("Klass: " + klass.upper() + "\n")
    if menu:
        print(menu_list)
    #pass

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
        print(class_name + " loaded.")
        if not merging:
            klass = class_name
        else:
            klass = klass + " & " + class_name
        return class_list
    except:
        print("Klassen hittades inte, försök igen.")
        get_class()

def get_int_input(text):
    valid = False
    while not valid:
        _input = input(text)
        try:
            _input = int(_input)
            valid = True
        except:
            print("Ogiltigt val, försök igen.")
    return _input

def random_student(class_list):
    cls()
    try:
        print("Slumpad elev: " + choice(class_list))
    except Exception as e:
        print("Något gick fel, försök igen.")
    print("\nTryck enter för att fortsätta")
    while True:
        if keyboard.is_pressed('enter'):
            pass

def change_class():
    cls(all = True, menu = False)
    class_list = get_class()
    return class_list

keyboard.add_hotkey('2', change_class)

def menu():
    class_list = get_class()
    keyboard.add_hotkey('1', random_student, args=(class_list))
    keyboard.add_hotkey('2', change_class)
    keyboard.add_hotkey('3', print, args=('triggered', 'hotkey'))
    while True:
        cls()
        while True:
            if keyboard.is_pressed('1'):
                random_student(class_list)
                break
            if keyboard.is_pressed('2'):
                cls(all = True, menu = False)
                class_list = get_class()
                break
            if keyboard.is_pressed('3'):
                cls()
                class_list += get_class(merging = True)



try:
    menu()
except KeyboardInterrupt:
    pass
