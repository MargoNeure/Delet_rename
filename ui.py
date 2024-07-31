from logger import input_data, print_data, rename_data, delet_data



def interface():
    print("Добрый день! Я бот. \n 1 - запись данных \n 2 - вывод данных \n 3 - изменить данные \n 4 - удалить данные")
    command = int(input("введите число "))

    while command != 1 and command != 2 and command != 3 and command != 4:
        print("Ошибка ввода")
        command = int(input("введите число "))

    if command == 1:
        input_data()
    if  command == 2:
        print_data()
    if command == 3:
        rename_data()
    if command == 4:
        delet_data()





interface()

