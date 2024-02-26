i = 1
while i < 6:
    print(i)
    if i == 4:
        break
    i += 1

x = 0
while x < 6:
    x += 1
    if x == 4:
        continue
    print(x)

y = 0
while y < 6:
    print(y)
    y += 1
else:
    print("no more")

songs = ["Calling", "Metro", "Outlaw"]
for x in songs:
    print(x)
    if x == "Metro":
        break

for x in songs:
    if x == "Metro":
        break
    print(x)

for i in range(2, 10, 2):
    print(i)
else:
    print("Thats all")

for m in range(7):
    if m == 4:
        break
    print()

m = ["red", "yellow", "orange"]
b = ["one piece", "Pokemon", "Naruto"]
for x in m:
    for y in b:
        print(m, b)

for x in [1, 2, 3]:
    pass