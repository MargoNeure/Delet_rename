from data_create import name_data, surname_data, phone_data, address_data

def input_data():
    name = name_data()
    surname =  surname_data()
    phone = phone_data()
    address = address_data()
    var = int(input(f"в каком формате  \n\n"
    f"1 вариант: \n"
    f"{name}\n{surname}\n{phone}\n{address}\n\n"
    f"2 вариант: \n"
    f"{name};{surname};{phone};{address}\n\n"
    f"выбери вариант  "))

    while var != 1 and var != 2:
        print("Ошибка ввода")
        var = int(input("введите число "))

    if var == 1:
        with open('tel1.csv', 'a', encoding = 'utf-8') as f :
            f.write(f"{name}\n{surname}\n{phone}\n{address}\n\n")
    elif var == 2:
        with open('tel2.csv', 'a', encoding = 'utf-8') as f :
            f.write(f"{name};{surname};{phone};{address}\n\n")



def print_data():
    print('данные из файла 1:  \n')
    with open('tel1.csv', 'r', encoding = 'utf-8') as f :
        tel1 = f.readlines()
        tel1_list = []
        j = 0
        for i in range(len(tel1)):
            if tel1_list == "\n" or i == len(tel1) - 1:
                tel1_list.append("".join(tel1[j:i+1]))
                j = i
        print("".join(tel1_list))

    print('данные из файла 2:  \n')
    with open('tel2.csv', 'r', encoding = 'utf-8') as f :
        tel2 = f.readlines()
        print(*tel2)

 
def delet_data():
    v = int(input("В каком файле хотите удалить данные?  \n"))
    while v != 1 and v != 2:
        print("Ошибка ввода")
        v = int(input("введите число "))

    if v == 1:
        with open('tel1.csv', 'r', encoding = 'utf-8') as f :
            tel1 = f.readlines()
            tel1_count = len(tel1)
            print(tel1_count)
            print(f"Количество записей в файле: {tel1_count/5}")
            y = int(input("Какую запись удалить? "))
            t = int(input("Выберите, что Вы хотите удалить: 1 - Имя, 2 - Фамилию, 3 - Телефон, 4 - Адрес, 0 - удалить всю запись "))
            while t != 1 and t != 2 and t != 3 and t != 4 and t!= 0:
                print("Ошибка ввода")
                t = int(input("введите число "))
            if t == 0:
                i = 1
                for i in range(i,6):
                    del tel1[(y-1)*5]
                    i += 1

            elif t != 0:
                tel1[(y-1)*5+t-1] == '\n'

        with open('tel1.csv', 'w') as f:
            f.writelines(tel1)


    elif v == 2:
        with open('tel2.csv', 'r', encoding = 'utf-8') as f :
            tel2 = f.readlines()
            tel2_count = len(tel2)
            print(f"Количество записей в файле: {tel2_count/2}")
            l = int(input("Какую запись удалить? "))
            m = int(input("Выберите, что Вы хотите удалить: 1 - Имя, 2 - Фамилию, 3 - Телефон, 4 - Адрес, 0 - удалить всю запись "))
            while m != 1 and m != 2 and m != 3 and m != 4 and m != 0:
                print("Ошибка ввода")
                m = int(input("введите число "))
            if m == 0:
                print(tel2[(l-1)*2])
                i = 0
                for i in range(i,2):
                    del tel2[(l-1)*2]
                    i += 1
            elif m != 0:
                elements = tel2[l].split(";")
                elements[m-1] = ' '
                tel2[l] = ';'.join(elements)
        
        with open('tel2.csv', 'w') as f:
            f.writelines(tel2)




delet_data()






            
