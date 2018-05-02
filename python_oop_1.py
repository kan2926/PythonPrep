class Employee:
    num_of_emps = 0
    raise_amt = 1.06
    def __init__(self, first_name, last_name, pay):
        self.first_name = first_name
        self.last_name = last_name
        self.pay = pay
        self.email = first_name +'.'+last_name+'@gmail.com'
        
        Employee.num_of_emps += 1

    def full_name(self):
        return '{} {}'.format(self.first_name, self.last_name)

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amt)

    @classmethod
    def set_raise(cls, amount):
        cls.raise_amt = amount
        

emp1 = Employee('A','B',10000)
print(emp1.email)
print(emp1.pay)
emp1.apply_raise()
print(emp1.pay)
print(emp1.__dict__)

emp2 = Employee('Test', 'Yahoo', 30000)
emp2.raise_amt = 2.02
print(emp2.__dict__)
print(Employee.num_of_emps)

print(Employee.raise_amt)
print(emp1.raise_amt)
print(emp2.raise_amt)

Employee.set_raise(2.44)

print(Employee.raise_amt)
print(emp1.raise_amt)
print(emp2.raise_amt)
