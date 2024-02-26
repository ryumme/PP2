x = lambda a : a + 10
print(x(5))

y = lambda c, b : c * b
print(y(4, 5))

z = lambda q, w, e : q + w + e
print(z(2, 4, 10))

def func(n):
    return lambda a : a * n

mydoubler = func(2)

print(mydoubler(11))