


if __name__ == '__main__':
    data = ["MMMSXXMASM",
            "MSAMXMSMSA",
            "AMXSXMAAMM",
            "MSAMASMSMX",
            "XMASAMXAMM",
            "XXAMMXXAMA",
            "SMSMSASXSS",
            "SAXAMASAAA",
            "MAMMMXMMMM",
            "MXMXAXMASX"]
    if True:
        data = []
        with open("inputs/day4.txt", "r") as input_file:
            for line in input_file:
                data.append(line)

    count = 0
    to_match = ["XMAS", "XMAS"[::-1]]
    match_length = len(to_match[0])
    matrix = [0, 0, 0, 0]
    for y in range(len(data)):
        for x in range(len(data[y])):
            # skip letters that can't be the start of a match
            if data[y][x] is not to_match[0][0] and data[y][x] is not to_match[1][0]:
                continue

            # check horizontal ahead
            to_test = data[y][x:x+4]
            if to_test in to_match:
                count += 1
                matrix[0] += 1
            # if we have 3 vertical lines ahead...
            if y + match_length <= len(data):
                # check vertical down behind
                if x > 2:
                    to_test = "".join([data[y + i][x - i] for i in range(match_length)])
                    if to_test in to_match:
                        count += 1
                        matrix[3] += 1

                # check vertical downwards
                to_test = "".join([data[y + i][x] for i in range(match_length)])
                if to_test in to_match:
                    count += 1
                    matrix[1] += 1

                # if we also have 3 horizontal ahead...
                if x + match_length <= len(data[y]):
                    # check vertical down ahead
                    to_test = "".join([data[y + i][x + i] for i in range(match_length)])
                    if to_test in to_match:
                        count += 1
                        matrix[2] += 1
    print("[Part 1] Count:", count, "h:{0} v:{1} ha:{2} hb:{3}".format(*matrix))

    count = 0
    to_match = ["MAS", "MAS"[::-1]]
    match_length = len(to_match[0])
    for y in range(len(data)):
        for x in range(len(data[y])):
            # skip letters that can't be the start of a match
            if data[y][x] is not to_match[0][0] and data[y][x] is not to_match[1][0]:
                continue

            if x + match_length > len(data[y]):
                continue
            if y + match_length > len(data):
                continue

            line_1 = "".join([data[y + i][x + i] for i in range(match_length)])
            line_2 = "".join([data[y + i][x+ 2 - i ] for i in range(match_length)])

            if (line_1 in to_match) and (line_2 in to_match):
                count += 1
    print("[Part 2] Count:", count)
