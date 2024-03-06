s = str(input())

x = 0
y = 0

for i in s:
    if i.isupper():
        x += 1
    elif i.islower():
        y += 1

print(x)
print(y)