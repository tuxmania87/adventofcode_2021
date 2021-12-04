# Part 1
f = open("three_input.txt","r")


numbers = list()

for line in f.readlines():
    numbers.append(line)

gamma = ""
epsilon = ""


for i in range(len(numbers[0])-1):
    ones = 0

    for number in numbers:
        if number[i] == "1":
            ones += 1

    if ones > len(numbers)/2:

        gamma += "1"
        epsilon += "0"
    else:
        gamma += "0"
        epsilon += "1"

    
print(int(gamma, 2) * int(epsilon, 2))


# Part 2
f = open("three_input.txt","r")


numbers = list()

for line in f.readlines():
    numbers.append(line)


# oxygen rating 

print(numbers)

digit = 0

numbers_copy = numbers.copy()

while len(numbers) > 1 and digit < len(numbers[0])-1:

    ones = 0
    keep = list()
    print("Debug run", digit)

    for number in numbers:
        if number[digit] == "1":
            ones += 1

    print("Debug ", digit, " ", ones, " ", ones < len(numbers)/2)



    for number in numbers:
        if ones < len(numbers)/2 and number[digit] == "0":
            keep.append(number)
        elif ones >= len(numbers)/2 and number[digit] == "1":
            keep.append(number)
    numbers = keep.copy()
    digit += 1

oxygen = (int(numbers[0],2))


# co2 rating 



print(numbers)

numbers = numbers_copy.copy()

digit = 0


while len(numbers) > 1 and digit < len(numbers[0])-1:

    ones = 0
    keep = list()
    print("Debug run", digit)

    for number in numbers:
        if number[digit] == "1":
            ones += 1

    print("Debug ", digit, " ", ones, " ", ones < len(numbers)/2)

    for number in numbers:
        if ones < len(numbers)/2 and number[digit] == "1":
            keep.append(number)
        elif ones >= len(numbers)/2 and number[digit] == "0":
            keep.append(number)
    numbers = keep.copy()
    digit += 1

co2 = (int(numbers[0],2))

print(co2 * oxygen)


