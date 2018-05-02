#!/bin/python3

import os
import sys
from time import strptime, strftime

#
# Complete the timeConversion function below.
#
def timeConversion(s):
    #
    # Write your code here.
    #
    print( strftime('%H:%M:%S', strptime(s,'%I:%M:%S%p')))
    return None
           
if __name__ == '__main__':

    s = input()

    result = timeConversion(s)

    print(result + '\n')
