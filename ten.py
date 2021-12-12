import numpy as np

f = open("ten_input.txt","r")


def handle_line(line):
    stack = list()

    for char in line.replace("\n",""):
        if char in ["(", "{", "<", "["]:
            stack.append(char)

        else:
            if char == ")" and stack[-1] == "(":
                stack.pop()
            elif char == "]" and stack[-1] == "[":
                stack.pop()
            elif char == ">" and stack[-1] == "<":
                stack.pop()
            elif char == "}" and stack[-1] == "{":
                stack.pop()
            else:
                return "corrupt", char
        
    
    if len(stack) == 0:
        return "complete", None
    return "incomplete", ''.join(stack)


sum1 = 0
sum2 = list()
for line in f.readlines():
    state, char = handle_line(line)

    print(state, char)
    
    if(char == ")"):
        sum1 += 3
    elif(char == "]"):
        sum1 += 57
    elif(char == "}"):
        sum1 += 1197
    elif (char==">"):
        sum1 += 25137
    elif len(char) > 1:

        subsum = 0
        reversed_string = char[::-1]
        print(reversed_string)
        for c in reversed_string:
            if(c == "("):
                subsum = subsum * 5 + 1
            elif(c == "["):
                subsum = subsum * 5 + 2
            elif(c == "{"):
                subsum = subsum * 5 + 3
            elif (c=="<"):
                subsum = subsum * 5 + 4
        sum2.append(subsum)





print("Part 1",sum1)
print("Part 2", int(np.median(sum2)))

    

