def solve(numheads, numlegs):
    for chickens in range(numheads + 1):
        rabbits = numheads - chickens
        if (chickens * 2 + rabbits * 4) == numlegs:
            print(f"Rabbits: {rabbits}, Chickens: {chickens}")

numheads = 35
numlegs = 94
solve(numheads,numlegs)