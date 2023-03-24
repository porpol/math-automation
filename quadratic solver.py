import math

print('Input a')
a = int(input())

print('Input b')
b = int(input())

print('Input c')
c = int(input())

x = (-b+math.sqrt(b*b-(4*a*c)))/2*a
x2 = (-b-math.sqrt(b*b-(4*a*c)))/2*a

print(x, x2)