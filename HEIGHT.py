from collections import Iterable
import os
# L = list(range(100))
# # print(L)
# # print(L[:10:2])
#
# d = {'a':1,'b':2,'c':3}
# for key in d:
#     print(key)
#
# for value in d.values():
#     print(value)
#
#
# print(isinstance('abc',Iterable))
# for i,value in enumerate(['A','B','C']):
#     print(i,value)
# print([x*x for x in range(1,11)])
#
# print([m+n for m in 'ABC' for n in 'abc'])
#
# print([d for d in os.listdir('.')])

# d = {'X':'A','Y':'B','Z':'C'}
# for k,v in d.items():
#     print(k,'=',v)

g = (x*x for x in range(10))
print(g)
for x in g:
    print(x)