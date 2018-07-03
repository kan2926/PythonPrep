import math
import os
import random
import re
import sys

# Complete the pickingNumbers function below.
def pickingNumbers(l):
    maximum=0
    for i in l:
        c=l.count(i)
        d=l.count(i-1)
        print(c)
        print(d)
        c=c+d
        print('sssss ',c)
        if c > maximum:
            maximum=c
    print(maximum)
            
    
if __name__ == '__main__':

    n = int(input())

    a = list(map(int, input().rstrip().split()))

    result = pickingNumbers(a)

    print(str(result) + '\n')
