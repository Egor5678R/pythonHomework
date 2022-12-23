#Напишите программу, которая будет преобразовывать десятичное число в двоичное.

#Пример:

#- 45 -> 101101
#- 3 -> 11
#- 2 -> 10

number1=int(input())
number2=""

while number1!=0:
    number2=str(number1%2)+number2
    number1=number1//2
    
print(f"| \nv \n{number2}")