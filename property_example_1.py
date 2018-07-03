class Celsius:
    def __init__(self, temp = 0):
        self.temp = temp

    def to_fahrenheit(self):
        return (self.temp * 1.8 ) + 32
    @property
    def temperature(self):
        print('get')
        return self.temp
    @temperature.setter
    def temperature(self, value):
        print('set')
        if value < -273:
            raise ValueError("Temperature below -273 is not possible")
        self.temp = value


m = Celsius()
m.temp = 37
print(m.temp)
print(m.to_fahrenheit())
print(m.__dict__)

c = Celsius(-277)
print(c.temp)
c.temp = -300
