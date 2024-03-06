import math
import time

num = int(input())
millisec = int(input())

time.sleep(millisec / 1000)
res = math.sqrt(num)

print(f"Square root of {num} after {millisec} milliseconds is {res}")