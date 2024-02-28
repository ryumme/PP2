import re

def snake(s):
    return re.sub("(?!^)(?=[A-Z])", '_', s).lower()

f = open('row.txt', encoding='utf-8')
s = str(f.read())
ans = snake(s)

print(ans)
