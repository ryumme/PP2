def fahr(cent):
    x = (5 / 9) * (cent - 32)
    print("Temperature in centigrade: {}".format(x))
temp = int(input())
fahr(temp)