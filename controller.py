#модель объединяющая все модули

from import_data import import_data
from export_data import export_data
from print_data import print_data
from cerch_data import search_data

#import model
#import veiw

def greeting():
    print("Добро пожаловать в журнал!")

def input_data():
    last_name = input("Введите фамилию: ")
    first_name = input("Введите имя: ")
    lesson = input("Введите предмет: ")
    rating = input("Введите оценку: ")
    return [last_name, first_name, lesson, rating]

def choice_sep():
    sep = input("Введите разделитель: ")
    if sep == "":
        sep = None
    return sep

def choice_todo():
    print("Доступные операции с журналом:\n\
    1 - добавить ученика, предет, оценку;\n\
    2 - показать ученика с его оценками;\n\
    3 - поиск ученика.")
    ch = input("Введите цифру: ")
    if ch == '1':
        sep = choice_sep()
        import_data(input_data(), sep)
    elif ch == '2':
        data = export_data()
        print_data(data)
    else:
        word = input("Введите данные для поиска: ")
        data = export_data()
        item = search_data(word, data)
        if item != None:
            print("Фамилия".center(20), "Имя".center(20), "предмет".center(15), "оценка".center(5))
            print("-"*130)
            print(item[0].center(20), item[1].center(20), item[2].center(15), item[3].center(5))
        else:
            print("Данные не обнаружены")


