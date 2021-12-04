# Part 1
f = open("two_input.txt","r")



x = 0
y = 0


for line in f.readlines():
    direction, amount = line.split(" ")

    if direction == "forward":
        x += int(amount)
    elif direction == "backward":
        x -= int(amount)
    elif direction == "down":
        y += int(amount)
    elif direction == "up":
        y -= int(amount)

print(x * y)


# Part 2
f = open("two_input.txt","r")



x = 0
y = 0
aim = 0


for line in f.readlines():
    direction, amount = line.split(" ")

    if direction == "forward":
        x += int(amount)
        y += aim * int(amount)
    elif direction == "backward":
        x -= int(amount)
    elif direction == "down":
        aim += int(amount)
    elif direction == "up":
        aim -= int(amount)

print(x * y)
