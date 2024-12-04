from operator import countOf

if __name__ == '__main__':
    list_a = []
    list_b = []

    with open("inputs/day1.txt", "r") as input_file:
        for line in input_file:
            data = line.split("   ")
            list_a.append(int(data[0]))
            list_b.append(int(data[1]))

    pairs = []

    list_a.sort()
    list_b.sort()
    for i in range(len(list_a)):
        pairs.append((list_a[i], list_b[i], abs(list_b[i] - list_a[i])))

    total_distance = sum(map(lambda p: p[2], pairs))
    print("[Part 1] Distance:", total_distance)

    scores = []
    for i in range(len(list_a)):
        current = list_a[i]
        amount = countOf(list_b, current)
        scores.append((current, current * amount))

    total_score = sum(map(lambda p: p[1], scores))
    print("[Part 2] Score:", total_score)
