n = int(input())
def func(n):
    for i in range(0, n + 1, 2):
        yield i

for num in func(n):
    print(num, end=", ")
