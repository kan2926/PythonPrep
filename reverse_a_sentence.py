


line = "Geek1 \nGeek2 \nGeek3";
print(line.split())
print(line.split(' ', 1))


l = "This is a house"
print(l.split())
print(l.split(' ',1))

a= 'anvitha'
print(a[::-1])


def reverse(a):
    if len(a) == 0:
        return a
    return reverse(a[1:])+ a[0]

print(reverse(a))
