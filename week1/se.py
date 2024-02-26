x = "Hello, World"
print(len(x))

txt = "Hello, World!"
a = txt[0]
print(a)

b = txt[2:5]
print(b)

c = txt.strip()
print(c)

txt = txt.upper()

txt = txt.lower()

txt = txt.replace("H", "J")

age = 36
txt = "Hello my name is John, and I am {}"
[print(txt.format(age))]