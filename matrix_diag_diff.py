#!/bin/python3

import os
import sys

#
# Complete the diagonalDifference function below.
#
def diagonalDifference(a): 
    diag1 = [ row[i] for i, row in enumerate(a) ]
    diag2 = [ row[-i-1] for i, row in enumerate(a)]
    return abs(sum(diag1) - sum(diag2))
    

if __name__ == '__main__':
    n = int(input())
    a = []
    for _ in range(n):
        a.append(list(map(int, input().rstrip().split())))
    result = diagonalDifference(a)
    print(result)
