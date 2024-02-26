import re

f = open("row.txt", encoding = 'utf-8')
s = str(f.read())

x = re.sub('_([a-z])', lambda match: match.gtoup(1).upper(), s)

print(x)