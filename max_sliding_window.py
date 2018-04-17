



s = [1,3,-1,-3,5,3,6,7]
w = int(input('Enter window size:'))
m = list()
for i in range(len(s)):
    m.append(max(s[i:i+w]))
    if i+w == len(s):
        break

print(m)
