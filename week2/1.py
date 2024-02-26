print(10 > 9)
print(10 == 10)
print(10 < 9)

a = 100
b = 33

if b > a:
    print("B is greater than A")
else:
    print("B is not greater than A")

print(bool("Hello"))
print(bool(15))

x = "Hello"
y = 15
print(bool(x))
print(bool(y))

bool("abc")
bool(123)
bool(["apple", "banana", "pineapple"])

bool(False)
bool(None)
bool(0)
bool("")
bool(())
bool([])
bool({})

def myfunc():
    return True

if myfunc():
    print("Yes")
else:
    print("No")

a = 200
print(isinstance(a, int))