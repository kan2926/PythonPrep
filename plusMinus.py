
import os
import sys

#
# Complete the plusMinus function below.
#
from decimal import Decimal
def plusMinus(arr):
    #
    # Write your code here.
    #
    n = len(arr)
    p_cnt = round((sum (i > 0 for i in arr)/n),6)
    n_cnt = round((sum (i < 0 for i in arr)/n),6)
    z_cnt = round((sum (i == 0 for i in arr)/n),6)
    print(p_cnt)
    print(n_cnt)
    print(z_cnt)   
    

if __name__ == '__main__':
    n = int(input())

    arr = list(map(int, input().rstrip().split()))
    print(arr)
    plusMinus(arr)

