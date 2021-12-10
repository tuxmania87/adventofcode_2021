
# part 1
f = open("nine_input.txt","r")


cols = list()

for line in f.readlines():
    cols.append([int(x) for x in line.replace("\n","")])




lowpoints = list()

for y in range(0,len(cols)):
    for x in range(0, len(cols[0])):

        candidates = [(x, y-1),(x, y+1),(x-1,y),(x+1,y)]

        something_is_lower = False

        for xc, yc in candidates:        
            if xc >= 0 and yc >= 0 and xc < len(cols[0]) and yc < len(cols):
                if cols[yc][xc] <= cols[y][x]:
                    something_is_lower = True
                    break

        if not something_is_lower:
            lowpoints.append((x,y))


print(lowpoints)

sum = 0
for x,y in lowpoints:
    sum += cols[y][x] + 1

print(sum)


import sys
sys.setrecursionlimit(10000) # 10000 is an example, try with different values

# part 2
print(cols)

def basin_rec(x, y, parent_value):

    #print("called for ", x, y, parent_value)

    if not cols[y][x] == 9 and (cols[y][x] - parent_value) == 1:
        candidates = [(x, y-1),(x, y+1),(x-1,y),(x+1,y)]
        
        sum = list()

        for xc, yc in candidates:        
            if xc >= 0 and yc >= 0 and xc < len(cols[0]) and yc < len(cols):
                sum += basin_rec(xc, yc, cols[y][x])


        #print("called for ", x, y, parent_value, "END", sum)
        return sum + [(x,y)]

    return []
        

results = list()
for x,y in lowpoints:

    ss = set(basin_rec(x, y, cols[y][x]-1))

    results.append(len(list(ss)))

    print("LP", x, y, len(list(ss)))


factor = 1
results.sort(reverse=True)
for elem in results[:3]:
    factor *= elem
    print(elem)

print(factor)
970200
486178