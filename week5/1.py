import re

f = open("row.txt", encoding = 'utf-8')
s = str(f.read())

x = re.search("ab*$", s)

if x:
    print("It's a match")
else:
    print("There is no match")