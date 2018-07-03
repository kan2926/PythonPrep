import itertools
import operator
a  = [2,3,5]
b = [6,7,8,9]

print(*(zip(a,b)))
print(*(itertools.zip_longest(a,b, fillvalue='*')))


print(*(itertools.product(a,b)))
print(*(itertools.permutations(a,3)))
print(*(itertools.combinations(a,2)))
print(*(itertools.combinations_with_replacement(a,2)))


l = [1,2,3,4]
print(*(itertools.accumulate(l)))
print(*(itertools.accumulate(l,operator.mul)))
