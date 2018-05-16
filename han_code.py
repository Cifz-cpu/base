from functools import reduce
def f(x):
    return x*x

r = map(f,[1,2,3,4,5,6,7,8,9])
# print(list(r))
def add(x,y):
    return x+y
print(reduce(add,[1,3,5,7,9]))