fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = []

for x in fruits:
  if "a" in x:
    newlist.append(x)
print(newlist)

newlistt = [x for x in fruits if x != "apple"]
print(newlistt)

newliist = [x for x in range(10) if x < 5]
print(newliist)

newwlist = [x if x != "banana" else "orange" for x in fruits]
print(newwlist)