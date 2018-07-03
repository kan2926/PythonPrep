import math
import os
import random
import re
import sys

# Complete the birthdayCakeCandles function below.
def birthdayCakeCandles(ar):
    max_element = max(ar)
    return ar.count(max_element)

if __name__ == '__main__':

    ar_count = int(input())

    ar = list(map(int, input().rstrip().split()))

    result = birthdayCakeCandles(ar)

    print(str(result) + '\n')
