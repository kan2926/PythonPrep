#import memory_profiler as mem_profile
import random
import time
import sys

names = ['A','B','C','D']
majors = ['a','b','c','d']

print('Memory Before {}Mb'.format(sys.getsizeof([])))
def people_gen(num_people):
    for i in range(num_people):
        person = { 'id': i, 'name': random.choice(names), 'majors':random.choice(majors)}
        yield person

t1 = time.clock()
people = people_gen(1000)
t2 = time.clock()
print('Memory after {} Mb'.format(sys.getsizeof([])))
