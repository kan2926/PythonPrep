
import sys
sys.stdout = open('closure_example2.log','w')


def outer_func(msg):
    def inner_func():
        print(msg)
    return inner_func

f = outer_func('Hi')
print(f.__name__)
f()
s = outer_func('Hello')
