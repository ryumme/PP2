def solve(numheads, numlegs):
    rabbits = (numlegs - 2 * numheads) // 2
    chickens = numheads - rabbits
    if rabbits >= 0 and chickens >= 0:
        return rabbits, chickens
    else:
        return None

heads, legs = 35, 94
chickens, rabbits = solve(heads, legs)
print("There are {} chickens and {} rabbits".format(chickens, rabbits))