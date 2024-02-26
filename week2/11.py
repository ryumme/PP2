mydict = {
    "brand" : "acer",
    "model" : "nitro5",
    "year" : 2021,
    "colors" : ["red", "black", "white"]
}
print(mydict)
print(mydict["brand"])

thisdict = dict(name = "Naruto", age = 19, country = "Konoha")
print(thisdict)

x = mydict["model"]
y = mydict.get("year")
z = mydict.keys()

print(x)
print(y)
print(z)

mydict["price"] = 300
print(mydict)

a = mydict.values()
print(a)

b = thisdict.items()
print(b)

mydict["year"] = 2023

mydict.update({"model" : "nitro6"})

mydict.popitem()

del mydict["year"]

mydict.clear()

for c in mydict:
    print(mydict[c])

for i, l in mydict:
    print(i, l)

ldict = mydict.copy()

mdict = dict(mydict)

