n = int(input())
def func(n):
    for i in range(0, n + 1, 1):
        if i % 3 == 0 and i % 4 == 0:
            yield i
for num in func(n):
    print(num)