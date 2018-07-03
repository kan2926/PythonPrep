from collections import deque
import itertools
def moving_average(iterable, n=3):
    # moving_average([40, 30, 50, 46, 39, 44]) --> 40.0 42.0 45.0 43.0
    # http://en.wikipedia.org/wiki/Moving_average
    it = iter(iterable)
    d = deque(itertools.islice(it, n-1))
    print(d)
    d.appendleft(0)
    print(d)
    s = sum(d)
    print(s)
    for elem in it:
        s += elem - d.popleft()
        print('1---',s)
        d.append(elem)
        yield s / float(n)


print(*(moving_average([40,30,50,46,39,44])))
