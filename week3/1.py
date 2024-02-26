def myfunc():
    print("Hi")

myfunc()

def func(fname):
    print(fname + " dope")

func("Naruto")
func("Natsu")
func("PP")

def names(*manes):
    print("The name is " + manes[2])

names("Emil", "Argus", "Peter")

def manes(mane1, mane2, mane3):
    print("The name is " + mane3)

manes(mane1 = "Jamal", mane2 = "Peter", mane3 = "Alim")

def py(**kids):
    print("My last name is " + kids["lname"])

py(fname = "Tobias", lname = "Gumball")

def country(country = "Kazakhstan"):
    print("I am from " + country)

country("Korea")
country("China")
country()
country("japan")

def fruts(food):
    for x in food:
        print(x)

fruits = ["apple", "orange", "dragon fruit"]
fruts(fruits)

def mofun(x):
    return 10 * x

print(mofun(2))
print(mofun(5))

def th_recur(k):
    if(k > 0):
        result = k + th_recur(k - 1)
        print(result)
    else:
        result = 0
    return result

th_recur(6)