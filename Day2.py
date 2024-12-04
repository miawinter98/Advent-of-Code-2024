from enum import Enum

class Mode(Enum):
    Unknown = 0,
    Increasing = 1,
    Decreasing = 2

def check_levels(first, second, current_mode):
    diff = abs(first - second)
    if diff < 1 or diff > 3:
        print("diff incorrect:", first, "and", second, "(" + str(diff) + ")")
        return False, current_mode

    if current_mode is Mode.Unknown:
        if first < second:
            return True, Mode.Increasing
        else:
            return True, Mode.Decreasing
    elif current_mode is Mode.Increasing and first > second:
        print("expected increasing, got decreasing:", first, "and", second)
        return False, current_mode
    elif current_mode is Mode.Decreasing and first < second:
        print("expected decreasing, got increasing:", first, "and", second)
        return False, current_mode

    return True, current_mode

def check_report(report):
    mode = Mode.Unknown
    for i in range(len(report)):
        a = report[i - 1]
        b = report[i]
        if i == 0:
            continue
        (is_save, mode) = check_levels(a, b, mode)
        if is_save is False:
            return False
    return True

def part1(data):
    save_count = 0
    for report in data:
        if check_report(report):
            save_count += 1
        else:
            print(report, "is not save")

    print("[Part 1] Save:", save_count, "out of", len(data))

def part2(data):
    save_count = 0
    for report in data:
        if check_report(report):
            save_count += 1
        else:
            is_save_with_dampener = False
            for i in range(len(report)):
                r = list(report)
                del r[i]
                if check_report(r):
                    is_save_with_dampener = True
                    break
            if is_save_with_dampener:
                save_count += 1
            else:
                print(report, "is not save (even with dampener)")



    print("[Part 2] Save:", save_count, "out of", len(data))

if __name__ == '__main__':
    input_data = [
        (7, 6, 4, 2, 1),
        (1, 2, 7, 8, 9),
        (9, 7, 6, 2, 1),
        (1, 3, 2, 4, 5),
        (8, 6, 4, 4, 1),
        (1, 3, 6, 7, 9),
    ]

    if True:
        input_data.clear()
        with open("inputs/day2.txt", "r") as input_file:
            for line in input_file:
                d = line.split(" ")
                input_data.append(tuple(map(lambda num: int(num), d)))

    part2(input_data)