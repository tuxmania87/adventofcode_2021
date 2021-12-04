import itertools

# Part 1
f = open("four_input.txt","r")


first_line = True


draw_sequence = list()

all_boards = list()
board = list()



for line in f.readlines():
    if first_line:

        draw_sequence = [int(x) for x in line.split(",")]

    elif line == "\n":
        if len(board) > 0:
            all_boards.append(board)
        board = list()
    else:
        board.append([int(x) for x in line.split()])

    first_line = False


def find_bingo(number_list, boards, abort_after_first_win):

    drawn_numbers = list()

    winner_list = list()

    for current_number in number_list:

        drawn_numbers.append(current_number)

        # search all boards

        board_counter = 0
        for board in boards:
            board_counter += 1

            # look for all rows if matching 100%  
            for row in board:

                if set(row) - set(drawn_numbers) == set():

                    # winner found, sum all unmarked numbers
                    # take all numbers in one big set and substract drawn_numbers

                    all_numbers = list(itertools.chain.from_iterable(board))

                    bingo_number = sum(list(set(all_numbers) - set(drawn_numbers))) * current_number

                    if board_counter not in winner_list:
                        winner_list.append(board_counter)

                    # check if all boards have won now
                    if len(winner_list) == len(boards):
                        # this winner is the last one
                        print("Last Winner", bingo_number, board_counter)
                        return bingo_number
                    
                    if abort_after_first_win:
                        return bingo_number
            
            # do the same for columns by transposing rows into columns

            transposed_board = list(map(list, zip(*board)))
            for row in transposed_board:

                if set(row) - set(drawn_numbers) == set():

                    # winner found, sum all unmarked numbers
                    # take all numbers in one big set and substract drawn_numbers

                    all_numbers = list(itertools.chain.from_iterable(board))

                    bingo_number = sum(list(set(all_numbers) - set(drawn_numbers))) * current_number

                    if board_counter not in winner_list:
                        winner_list.append(board_counter)

                    # check if all boards have won now
                    if len(winner_list) == len(boards):
                        # this winner is the last one
                        print("Last Winner", bingo_number, board_counter)
                        return bingo_number


                    
                    if abort_after_first_win:
                        return bingo_number






print(find_bingo(draw_sequence, all_boards, True))

print("Part two")

find_bingo(draw_sequence, all_boards, False)



