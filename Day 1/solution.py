def main():
    list1 = []
    list2 = []

    with open("Day 1/input.txt") as file:
        for line in file:
            a, b = line.split()
            list1.append(int(a))
            list2.append(int(b))
        list1.sort()
        list2.sort()
        distance = 0

        for item in zip(list1, list2):
            distance += abs(item[0] - item[1])
        print(f"Part1: Distance is {distance}")

if __name__ == "__main__":
    main()