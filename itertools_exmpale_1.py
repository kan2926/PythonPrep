from itertools import *

li = [2, 4, 12, 24, 5, 7, 8, 10, 20,32,12,4,5,67,89,10,90]
print ("The sliced list values are : ",end="")
print (list(islice(li,4, 12)))

print(list(takewhile(lambda x: x%2 ==0, li)))
print(list(dropwhile(lambda x:x%2 ==0, li)))
print (*(zip('GesoGes','ekfrek')))
