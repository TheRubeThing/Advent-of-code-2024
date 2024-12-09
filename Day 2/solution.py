test_data = """7 6 4 2 1
1 2 7 8 9
9 7 6 2 1
1 3 2 4 5
8 6 4 4 1
1 3 6 7 9
4 5 3 2 1 
2 1 3 4 5
2 1 2 3 4
5 1 2 3 4
1 5 4 3 2
10 5 4 3 2
5 10 12 13 14"""

min_safe_step = 1
max_safe_step = 3

def sign(x):
    return 0 if x == 0 else x / abs(x)

def part1(test_data):
    reports = [[int(level) for level in report.split()] for report in test_data.split("\n")]
    safe_reports = [check_safe2(report) for report in reports]
    print(f"P1: {safe_reports.count(True)}")

def is_level_difference_unsafe(diff):
    return abs(diff) > max_safe_step or abs(diff) < min_safe_step

def is_level_direction_unsafe(diff, dir):
    diff_dir = sign(diff)
    return diff_dir != dir

def check_safe2(report):
    # check peak
    dirs = [sign(report[i] - report[i - 1]) for i in range(1, len(report))]
    ignore_idx = None
    count_neg = dirs.count(-1.0)
    count_pos = dirs.count(1.0)
    if count_neg == count_pos:
        return False
    elif count_neg > count_pos:
        if count_pos > 2:
            return False
        for i, dir in enumerate(dirs):
            if dir == 1.0:
                if i == len(dirs):
                    ignore_idx = i + 1
                else:
                    ignore_idx = i
    else:
        if count_neg > 2:
            return False
        for i, dir in enumerate(dirs):
            if dir == -1.0:
                if i == len(dirs):
                    ignore_idx = i + 1
                else:
                    ignore_idx = i
    
    if ignore_idx != None:
        report = report[0 : ignore_idx] + report[ignore_idx + 1 : len(report)]

    dampener = False if ignore_idx else True
    ignore_idx = None
    for i in range(1, len(report)):
        past_index = i - 1
        if ignore_idx and past_index == ignore_idx:
            past_index = i - 2
        diff = abs(report[i] - report[past_index])
        if diff < min_safe_step or diff > max_safe_step:
            if dampener:
                dampener = False
                ignore_idx = i
                continue
            return False
    return True


def main():
    with open("Day 2/input.txt") as test_file:
        test_data = test_file.read()
        part1(test_data)

if __name__ == "__main__":
    main()