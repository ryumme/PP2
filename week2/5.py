thislist = ["banana", "cherry", "apple"]
thislist.sort(reverse = True)
print(thislist)

def myfunc(n):
    return abs(n - 50)

thisslist = [100, 50, 68, 76, 25]
thisslist.sort(key = myfunc)
print(thisslist)

thislist.reverse()
print(thislist)


