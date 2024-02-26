x = "awesome"

def myfuc():
    print("Python is " + x)

myfuc()

x = "awesome"

def myfunc():
  x = "fantastic"
  print("Python is " + x)

myfunc()

print("Python is " + x)

def myfunc():
  global x
  x = "crazy"

myfunc()

print("Python is " + x)