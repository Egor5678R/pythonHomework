
import student_info as si
import cabinet_info as cab


def option():
    print("\nВвод данных производится вручную")
    choice = int(input(' \n \
    1: Поиск id студента по фамилии \n \
    2: Посмотреть класс  и место которое занимает студент \n \
    3: Выход\n \
    Ваш выбор: '))

    if choice == 1:
        Surn = str(input("Введите фамилию ученика: "))
        if Surn in si.studentCard['Фамилия']:
            index = si.studentCard['Фамилия'].index(Surn)
        print(f"{si.studentCard['ID'][index]}, {si.studentCard['Имя'][index]},{si.studentCard['Фамилия'][index]}\n,{si.studentCard['Дата рождения'][index]}, {si.studentCard['Успеваемость'][index]}")
        print('\nХотите выполнить какую-то другую операцию??? Да или Нет: ')
        num = input()
        if num == "да".lower():
            option()
        exit()

    elif choice == 2:
        c = input('Введите id студента для вывода по классам: ')
        if c in cab.classCard['ID']:
            index = cab.classCard['ID'].index(c)
            print(f" Сидит в классе - {cab.classCard['Предмет'][index]}\n\, за партой номер - {cab.classCard['Номер парты'][index]}, это {cab.classCard['Ряд'][index]}, парта - {cab.classCard['Вид парты'][index]}, Имя: {si.studentCard['Имя'][index]}, Фамилия - {si.studentCard['Фамилия'][index]}, и успеваемасть у студента: {si.studentCard['Успеваемость'][index]}")
            print('\nХотите выполнить другую операцию??? Y или N: ')
            num = input()
            if num == "да".lower():
                option()
            exit()
    else:
        print('еще раз')
    exit()


option()
