myset = {"this", "and", "that", "this", "and"}
print(myset)
print(type(myset))

for x in myset:
    print(x)

myset.add("dayumn")

anoth = ["daya", "tattakae", "joke"]

myset.update(anoth)
print(myset)

myset.remove("and")
print(myset)

myset.discard("that")
print(myset)

moset = {"yep", "haha", "this"}
set3 = myset.union(moset)
print(set3)

myset.intersection_update(moset)
print(myset)

myset.symmetric_difference_update(moset)
print(myset)




