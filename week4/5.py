n = int(input())
def func(n):
    for i in range(n + 1):
        yield(i ** 2)

for i in func(n):
    print(i)