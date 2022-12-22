#Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.

#Пример:

#- 6782 -> 23
#- 0,56 -> 11

number=input()

def summa(number):                            
    if float(number) < 0:                            
        x=float(x)*(-1)
    num=0

    for i in str(number):
        if i !='.':
            num+=int(i)
    return num

   
print(f'{number} -> {summa(number)}')