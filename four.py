# Part 1
f = open("four_input.txt","r")


line_number = 0


number_list = list()

boards = list()
board = list()

drawn_numbers = list()

for line in f.readlines():
    if line_number == 0:

        number_list = [int(x) for x in line.split(",")]

    elif line == "\n":
        if len(board) > 0:
            boards.append(board)
        board = list()
    else:
        board.append([int(x) for x in line.split()])



    line_number += 1

print(boards)

for current_number in number_list:

    drawn_numbers.append(current_number)

    # search all boards
    

    for board in boards:

        # look for all rows if matching 100%  
        for row in board:

            print(row, drawn_numbers)

            if set(row) == set(drawn_numbers):

                # winner found, sum all other rows and 
                # multiply by last drawn number

                sum = 0
                for row_it in board:
                    if row_it != row:
                        sum += sum(row_it)


                print("BINGO", sum * current_number)
            
        
        




