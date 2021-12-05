# Part 1


def number_of_overlaps(filename, diagonales=False):

    f = open(filename,"r")

    def swap(x,y):
        return y,x

    points = list()

    for line in f.readlines():
        start, end = line.replace("\n","").split(" -> ")

        xs, ys = start.split(",")

        xs = int(xs)
        ys = int(ys)

        xe, ye = end.split(",")

        xe = int(xe)
        ye = int(ye)


        #part 1 only if x = x or y = y
        if not ((xe == xs) or (ye == ys)):
            if not diagonales:
                continue
            else:
                #print("Diagonal", start, end)
                # case 1 ascending 45 degrees
                if xs == ys and xe == ye:
                    for ix in range(xs, xe+1):
                        points.append((ix, ix))
                # case 2 descending 45 degrees
                else:
                    correct_range_x = range(xs, xe+1) if xs < xe else (range(xs, xe-1, -1) if xs > xe else [xe])
                    correct_range_y = range(ys, ye+1) if ys < ye else (range(ys, ye-1, -1) if ys > ye else [ye])

                    for point in list(zip(list(correct_range_x), list(correct_range_y))):
                        points.append(point)
                            
        else:

            # possibly swap coordinates to make them appear in ascending order

            correct_range_x = range(xs, xe+1) if xs < xe else (range(xs, xe-1, -1) if xs > xe else [xe])
            correct_range_y = range(ys, ye+1) if ys < ye else (range(ys, ye-1, -1) if ys > ye else [ye])

            for ix in correct_range_x:
                for iy in correct_range_y:

                    points.append((ix, iy))


    # create dict of occurences

    groupy_map = {}

    for point in points:
        if point not in groupy_map.keys():
            groupy_map[point] = 0
        groupy_map[point] += 1


    counter = 0
    for k, v in groupy_map.items():
        
        if v >= 2:
            counter += 1

    return counter



part1 = number_of_overlaps("five_input.txt")
print("Part 1", part1)


part2 = number_of_overlaps("five_input.txt", True)
print("Part 2", part2)