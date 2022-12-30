#Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N

number = int(input("при N = "))
list = []

for i in range(2,number):
    k = False

    for j in range(2, i):
        if i % j == 0:
            k = True
            break

    if number % i == 0 and k == False:
        print(i,end=" ")

print("<-простые множетели")