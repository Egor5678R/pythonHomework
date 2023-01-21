'''N=int(input())
List=[1]

for i in range (1,4):
    List.append((i+1)*List [i-1])

print(f" {N} -> {List}")'''

from math import factorial

N = int(input())
print(list(map(lambda x: ((x == 1) and 1) or x * factorial(x - 1),list(range(1,N + 1)))))