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

# def power(x,n=2):
#     s = 1
#     while n>0:
#         s = x * s
#         n = n - 1
#     return s
#
# print(power(2))

def add_end(L = None):
    if L is None:
        L = []
    L.append('lxq')
    return L
# print(add_end())
# print(add_end())

# def calc (*numbers):
#     sum = 0
#     for n in numbers:
#         sum = sum + n
#     return sum
# num = [1,2,3,4,5,6,7,8,9]
# print(calc(*num))

def person(name,age,**kw):

    if 'city' in kw:
        print('city')

    print('name',name,'age',age,'other',kw)

# person('wz',18,city='New York',job='ShiZhang')
def fact_iter(n,pro):
    if n==1:
        return pro
    return fact_iter(n-1,n * pro)

def fact(n):
    return fact_iter(n,1)
print(fact(100))