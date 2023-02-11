#вывод данных

def print_data(data):
    if len(data) > 0:
        print("Фамилия".center(20), "Имя".center(20), "Предмет".center(15), "Оценка".center(5))
        print("-"*100)
        for item in data:
            print(item[0].center(20), item[1].center(20), item[2].center(20), item[3].center(5))
    else:
        print("журнал пуст!")