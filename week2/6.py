mylist = ["cherry", "pineapple", "dragon"]
mlist = mylist.copy()
print(mlist) 

molist = list(mylist)
print(molist)

nlist = [5, 3, 10]

for x in nlist:
    mylist.append(x)
print(mylist)

mylist.extend(nlist)
print(mylist)

