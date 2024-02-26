from datetime import *

firstInp = input()
secondInp = input()
firstDate = datetime.strptime(firstInp, "%d.%m.%Y")
secondDate = datetime.strptime(secondInp, "%d.%m.%Y")

delta = abs(secondDate - firstDate)
days = delta.days

print(days*24*60*60, "seconds")