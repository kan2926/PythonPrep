




k = input('Enter String 1:')
m = input('Enter String 2:')
l = [ord(i) for i in k]
m =  [ord(i) for i in m]
l.sort()
m.sort()
print('Given strings are Anagrams :', l == m)
