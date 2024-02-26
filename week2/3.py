mylist = ["banana", "cherry", "avocado"]
print(mylist)
print(len(mylist))
print(type(mylist))

list1 = ["abc", 34, True, 40, "male"]
print(type(mylist))

thislist = list(("apple", "banana", "cherry"))
print(thislist)

print(thislist[1])
print(thislist[-1])

thisslist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thisslist[2:5])
print(thisslist[:4])
print(thisslist[2:])
print(thisslist[-4:-1])

tthislist = ["apple", "banana", "cherry"]
if "apple" in tthislist:
    print("Yes, 'apple' is in the fruits list")

tthislist[1] = "orange"
print(tthislist)

thislistt = ["apple", "banana", "cherry"]
thislistt[1:3] = ["watermelon"]
print(thislistt)
thislistt.insert(2, "kiwi")
print(thislistt)
thislistt.append("pineapple")
print(thislistt)

thisliist = ["apple", "banana", "cherry"]
tropical = ["mango", "pineapple", "papaya"]
thisliist.extend(tropical)
print(thisliist)

thislisst = ["apple", "banana", "cherry"]
thistuple = ("kiwi", "orange")
thislisst.extend(thistuple)
print(thislisst)

thislisst.remove("banana")
print(thislisst)

thislisst.pop(0)
print(thislisst)

del thislisst

tthislist.clear()
print(tthislist)

for x in thislist:
    print(x)

for i in range(len(thislist)):
    print(thislist[i])

thiislist = ["apple", "banana", "cherry"]
i = 0
while i < len(thisliist):
  print(thisliist[i])
  i = i + 1

thisliist = ["apple", "banana", "cherry"]
[print(x) for x in thisliist]

