import time

# My first implementation of the problem
def first():
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

        ocurrances = 0
        occurance_cache = {}
        previous_list2_index = 0

        for i in range(len(list1)):
            if list1[i] in occurance_cache:
                ocurrances += occurance_cache[list1[i]] * list1[i]
            else:
                count = 0
                for j in range(previous_list2_index, len(list2)):
                    if list1[i] == list2[j]:
                        count += 1
                    elif list1[i] > list2[j]:
                        continue
                    else:
                        previous_list2_index = j
                        break

                ocurrances += list1[i] * count
                occurance_cache[list1[i]] = count

        print(f"Part2: Occurance is {ocurrances}")

# Wanted to see the performance without caching and storing the loop
# iterations
def simplified():
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

        ocurrances = 0
        for i in range(len(list1)):
            count = 0
            for j in range(len(list2)):
                if list1[i] == list2[j]:
                    count += 1

            ocurrances += list1[i] * count

        print(f"Part2: Occurance is {ocurrances}")

def time_function(func):
    start = time.time()
    func()
    end = time.time()
    print(f"Func {func} took {end - start} time")

def main():
    time_function(first)
    time_function(simplified)

if __name__ == "__main__":
    main()