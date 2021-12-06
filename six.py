from typing import List


f = open("six_input.txt","r")



fishy = [int(x) for x in f.readline().split(",")]



counter = {}

#init counter 
for i in range(0,9):
    counter[i] = 0

for fish in fishy:
    counter[fish] += 1
    


for day in range(256):

    if day == 80:
        print("part 1", sum(counter.values()))

    temp_counter = {}
    #init counter 
    for i in range(0,9):
        temp_counter[i] = 0

    for fish_val, amount in counter.items():

        if fish_val == 0:
            temp_counter[6] += amount
            temp_counter[8] += amount
        else:
            temp_counter[fish_val-1] += amount

        counter = temp_counter
    
print("part 2", sum(counter.values()))



