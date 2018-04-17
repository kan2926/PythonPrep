
def evaluate(expr):
    tmp = []
    delimeter = ','
    operators = {'+' : lambda y, x : x+ y,
                 '-' : lambda y, x: x-y,
                 '*': lambda y, x: x*y,
                 '/': lambda y,x : x/y
                 }
    for i in expr.split(delimeter):
        if i in operators:
            tmp.append(operators[i](tmp.pop(), tmp.pop()))
        else:
            tmp.append(int(i))
    return tmp[-1]

expr = input('Enter expression:')
print(evaluate(expr))
