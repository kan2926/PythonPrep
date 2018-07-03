import math
import os
import random
import re
import sys

# Complete the staircase function below.
def staircase(n):
    for i in range(1,n+1,1):
        st = [' ' for x in range(n-i)]
        st += ['#' for x in range(i)]
        print(''.join(st))

if __name__ == '__main__':
    n = int(input())

    staircase(n)
