import math
import os
import random
import re
import sys

### Complete the formingMagicSquare function below.

##    for i in range(len(s)):
##        row_sum = sum(s[i])
##        col_sum = sum([x[i] for x in s])
##        print("row_sum   ",i, ' ' ,row_sum )
##        print("col_sum   ",i, ' ' ,col_sum )
##    diag_sum_1 = sum([ row[i] for i,row in enumerate(s) ])
##    diag_sum_2 = sum([ row[-i-1] for i,row in enumerate(s) ])
##    print("diag_sum   ",diag_sum_1 )
##    print("diag_sum   ",diag_sum_2 )
def formingMagicSquare(s):
    pre = [
                [[8, 1, 6], [3, 5, 7], [4, 9, 2]],
                [[6, 1, 8], [7, 5, 3], [2, 9, 4]],
                [[4, 9, 2], [3, 5, 7], [8, 1, 6]],
                [[2, 9, 4], [7, 5, 3], [6, 1, 8]], 
                [[8, 3, 4], [1, 5, 9], [6, 7, 2]],
                [[4, 3, 8], [9, 5, 1], [2, 7, 6]], 
                [[6, 7, 2], [1, 5, 9], [8, 3, 4]], 
                [[2, 7, 6], [9, 5, 1], [4, 3, 8]],
                ]
    totals = []
    for p in pre:
        total = 0
        for i_row, j_row in zip(p, s):
            for i, j in zip(i_row, j_row):
                if not i == j :
                    total += max([i,j]) - min([i,j])
        totals.append(total)
    return min(totals)

if __name__ == '__main__':
    s = []
    for _ in range(3):
        s.append(list(map(int, input().rstrip().split())))

    result = formingMagicSquare(s)

    print(str(result) + '\n')
