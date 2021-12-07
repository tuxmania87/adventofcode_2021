

# part 1
f = open("seven_input.txt","r")


crabs = [int(x) for x in f.readline().split(",")]

print(crabs)

min_distance = 100000000
min_i = -1



for i in range(min(crabs), max(crabs)+1):

    distance = 0
    for c in crabs:
        distance += abs(c - i)


    if distance < min_distance:
        min_distance = distance
        min_i = i

print(min_distance)
    


# part 2
f = open("seven_input.txt","r")


crabs = [int(x) for x in f.readline().split(",")]

print(crabs)

min_distance = 1000000000000000000000000
min_i = -1


def gauss(n):
    return  int(( n *  (n-1) / 2))

for i in range(min(crabs), max(crabs)+1):

    distance = 0
    for c in crabs:
        distance += gauss(abs(c-i)+1)


    if distance < min_distance:
        min_distance = distance
        min_i = i

print(min_distance, min_i)
    