def sqaure(a, b):
    for i in range(a, b + 1):
        yield i ** 2

a = int(input())
b = int(input())

for i in sqaure(a, b):
    print(i)