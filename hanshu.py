import math


# def my_abs(x):
#
#     if not isinstance(x,(int,float)):
#
#         raise TypeError('bad operand')
#
#     if x >= 0:
#         return x
#     else:
#         return -x

# print(my_abs('a'))

# def soft():
#     pass
#
#
# def move(x,y,step,angle = 0):
#     nx = x + step * math.cos(angle)
#     ny = y - step * math.sin(angle)
#     return nx,ny
#
# print(move(100,100,60,math.pi / 6))

def power(x,n=2):
    s = 1
    while n>0:
        s = x * s
        n = n - 1
    return s

print(power(2))

