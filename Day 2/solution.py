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
5 10 12 13 14
10 12 13 14 20
20 18 16 14 8
6 1 7 8 9 10"""

min_safe_step = 1
max_safe_step = 3

def sign(x):
    return 0 if x == 0 else x / abs(x)

def part1(test_data):
    reports = [[int(level) for level in report.split()] for report in test_data.split("\n")]
    safe_reports = [check_safe(report) for report in reports]
    print(f"P1: {safe_reports.count(True)}")
    safe_reports_with_dampener = [check_safe_with_dampener(report) for report in reports]
    print(f"P2: {safe_reports_with_dampener.count(True)}")


def check_safe(report):
    dirs = []
    for i in range(1,len(report)):
        diff = report[i] - report[i-1]
        dir = sign(diff)
        if abs(diff) < min_safe_step or abs(diff) > max_safe_step:
            return False
        if len(dirs) > 0 and dir != dirs[-1]:
            return False
        dirs.append(dir)
    return True

def check_safe_with_dampener(report):
    dampener_unused = True
    steps = [report[i] - report[i-1] for i in range(1, len(report))]
    directions = [sign(report[i] - report[i-1]) for i in range(1, len(report))]
    general_direction = sign(sum(directions))
    for i, step, direction in zip(range(1, len(report)), steps, directions):
        if direction != general_direction:
            if dampener_unused:
                dampener_unused = False
                continue
            else:
                return False

        if abs(step) < min_safe_step or abs(step) > max_safe_step:
            if dampener_unused:
                dampener_unused = False
                if i == 1:
                    continue
                elif i != len(steps):
                    new_step = steps[i] + step
                    if abs(new_step) < min_safe_step or abs(new_step) > max_safe_step:
                        return False
            else:
                return False
    return True


def main():
        part1(test_data)

if __name__ == "__main__":
    main()