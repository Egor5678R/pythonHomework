#Вычислить число c заданной точностью d

#Пример:

#- при $d = 0.001, π = 3.141.$    $10^{-1} ≤ d ≤10^{-10}$

import math

number = float(input("при d = "))
a = 0

while number != int(number):
    a+=1
    number*=10

print("π =","{:.{}f}".format(math.pi,a))