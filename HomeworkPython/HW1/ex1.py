#Напишите программу, которая принимает на вход цифру, обозначающую день недели, и проверяет, является ли этот день выходным.
#Пример:
#- 6 -> да
#- 7 -> да
#- 1 -> нет
day=int(input("Введите число дня недели: "))

if day==6 or day==7:
 print("Вы ввели выходной день")
 
else:
 print("Вы ввели будний день или неизвесную цифру дня")