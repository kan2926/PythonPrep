from functools import wraps

def df(func):
    @wraps(func)
    def wf(*args, **kwargs):
        print('first {}'.format(func.__name__))
        return func(*args, **kwargs)
    return wf

def ds(func):

    @wraps(func)
    def wf(*args, **kwargs):
        print('second {}'.format(func.__name__))
        return func(*args, **kwargs)
    return wf

class dc:
    def __init__(self, func):
        self.func = func

    def __call__(self,*args, **kwargs):
        print('call before ')
        return self.func(*args, **kwargs)


@df
def display():
    print('display function ran')

@df
def mod():
    print('modify')


@df
@ds
def mod1(name, age):
    print('display name{}, age{}'.format(name, age))
   
mod1('John',33)
