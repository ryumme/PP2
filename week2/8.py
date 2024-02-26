fruits = ("cherry", "pineapple", "orange", "mandarin", "kurama")
(red, yellow, *orange) = fruits
print(orange)

for x in fruits:
    print(x)

for i in range(len(fruits)):
    print(fruits[i])

i = 0
while i < len(fruits):
    print(fruits[i])
    i = i + 1

