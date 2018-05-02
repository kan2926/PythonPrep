from collections import namedtuple

class Point(namedtuple('Point','x y')):
    __slots__ = ()
    @property
    def hypot(self):
        print(self.x,'***',self.y)
        return (self.x **5 + self.y **5) **0.5
    
    def __str__(self):
        return 'Point x = %6.4f y=%6.4f hypot=%6.3f ' % (self.x, self.y, self.hypot)

for p in Point(3,4), Point(4,5):
    print(p)
    
        
