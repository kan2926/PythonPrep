import re

print(r'\tTab')
print('\tTab')

pattern = re.compile(r'https?://(www\.)?(\w+)(\.\w+)')
text_to_search = '''
https://google.com
http://youtube.com
http://twitter.com

'''
sub_urls = pattern.sub(r'\2\3', text_to_search)
print(sub_urls)

matches = pattern.finditer(text_to_search)


for match in matches:
    print(match.group(2))


match = pattern.findall(text_to_search)
print(match)
s = "i-k42ki59"

l = list([int(float(s)) for s in re.findall(r'-?\d+\.?\d*', s)])
print(l)
