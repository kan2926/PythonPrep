def decorate_message(fun):
 
    # Nested function
    def addWelcome(site_name):
        return "Welcome to " + fun(site_name)
 
    # Decorator returns a function
    return addWelcome
 
@decorate_message
def site(site_name):
    return site_name;
 
# Driver code
 
# This call is equivalent to call to
# decorate_message() with function
# site("GeeksforGeeks") as parameter

def cube(x):
    return x**2

cubes = map(cube, range(10))
print(cubes)
 
print(site("GeeksforGeeks"))

print( (lambda x, y: x *y ) (4,5))
x = map(lambda x: x**2 , range(10))
print(x)

