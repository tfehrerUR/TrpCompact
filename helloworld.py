import numpy as np
lst = list(range(1,100,1))
print(lst)
def pri(x):
    c=-1
    for i in range(2, 100):
        if x%i == 0 :
            c=c+1
    return c
lst2 = map(pri, lst)
print(list(lst2))
