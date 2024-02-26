thistuple = ("fire", "dragon", "roar", "lightning", "storm")
print(len(thistuple))

print(type(thistuple))

print(thistuple[2:])
print(thistuple[:4])

if "dragon" in thistuple:
    print("Yes, yes it is")

thislist = list(thistuple)
thislist[1] = "god"
thislist.append("hand")
thistuple = tuple(thislist)
y = ("red",)
thistuple += y
print(thistuple)

del thistuple



