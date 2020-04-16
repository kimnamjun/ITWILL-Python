import re
a = ['a']

z = set()
for i in a:
    x = re.sub('a','b',i)
    z.add(x)

print(z)