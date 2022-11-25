[(x, y) for x in [1,2,3] for y in [3,1,4] if x != y]


# can also be implemented as :
combs = []
for x in [1,2,3]:
    for y in [3,1,4]:
        if x != y:
            combs.append((x, y))