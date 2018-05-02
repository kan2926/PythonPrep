import re

text_to_search = 'dsfjsld=4jj-46jfsljfs333ljglsjfl31slfkjsdlj43'

p = re.compile(r'\d+')
matches = p.finditer(text_to_search)
for i in matches:
    print(i)

l = list([int(float(s)) for s in re.findall(r'-?\d+', text_to_search)])
print(l)
