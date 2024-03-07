s = str(input("File name: "))

file = open(s, "r")

sum = 0
for i in file:
    sum += 1

print(sum)