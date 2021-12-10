
from collections import Counter
# part 1
f = open("eight_input.txt","r")


sum = 0

for line in f.readlines():
    patterns, output = line.split(" | ")

    for out in output.split():
        if len(out) in [2,4,3,7]:
            sum += 1

    

print("Part 1", sum)


# part 2
f = open("eight_input.txt","r")


sum = 0


one = set()
two = set()
three = set()
four = set()
five = set()
six = set()
seven = set()
eight = set()
nine = set()
zero = set()



for line in f.readlines():
    patterns, output = line.split(" | ")

    digit_map = {}

    for out in patterns.split():

        if len(out)  == 2:
            one = set([x for x in out])
        elif len(out)  == 4:
            four = set([x for x in out])
        if len(out)  == 3:
            seven = set([x for x in out])
        if len(out)  == 7:
            eight = set([x for x in out])

        else:
            if len(out) not in digit_map:
                digit_map[len(out)] = list()

            digit_map[len(out)].append(set([x for x in out]))
        

    # nine is the one with total of 6 segments
    # but not containing fully the 2 segments of the one

    leftovers = list()

    for sixers in digit_map[6]:
        if not (one - sixers == set()):
            six = sixers
        else:
            leftovers.append(sixers)

    # the 4 is fully integrated in 9 therefore
    # if set substraction is empty, it must be nine

    for sixers in leftovers:
        if four - sixers == set():
            nine = sixers
        else:
            zero = sixers

    # get the bottom left digit that is contained by the 2
    # then we can identify the 2 because its the only 5 digit number
    # containing that segment

    leftovers = list()

    bottomleft = next(iter((eight - nine)))

    for fivers in digit_map[5]:


        if bottomleft in fivers:
            two = fivers
        else:
            leftovers.append(fivers)


    # identify top right segment

    topright = next(iter(one.intersection(two)))

    # topright is only contained by the 3, the other has to be the 5

    for fivers in leftovers:
        if topright in fivers:
            three = fivers
        else:
            five = fivers

    
    # calculate output number
    out_string = ""

    for out in output.split():
        if set(out) == one:
            out_string += "1"
        elif set(out) == two:
            out_string += "2"
        elif set(out) == three:
            out_string += "3"
        elif set(out) == four:
            out_string += "4"
        elif set(out) == five:
            out_string += "5"
        elif set(out) == six:
            out_string += "6"
        elif set(out) == seven:
            out_string += "7"
        elif set(out) == eight:
            out_string += "8"
        elif set(out) == nine:
            out_string += "9"
        elif set(out) == zero:
            out_string += "0"
        
    sum += int(out_string)


print("Part 2", sum)






