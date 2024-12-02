from copy import deepcopy


def read_reports(filename: str):
    reports = []
    with open(filename, 'r') as file:
        content = file.readlines()
        for line in content:
            reports.append([int(i) for i in line.split(' ')])
    return reports


def analyze_report(report: list[int]) -> int:
    mode = None
    for idx in range(len(report) - 1):
        l, r = report[idx], report[idx + 1]
        if abs(l - r) > 3 or l == r:
            return 0
        elif l < r:
            if mode == 'up':
                return 0
            mode = 'down'
        elif l > r:
            if mode == 'down':
                return 0
            mode = 'up'
    return 1


def analyze_dampened(report: list[int]) -> int:
    is_safe = analyze_report(report)
    if is_safe:
        return 1
    # If needed, we start dampening by removing out one level at a time from LTR.
    for x in range(len(report)):
        report_copy = deepcopy(report)
        del report_copy[x]
        is_safe = analyze_report(report_copy)
        if is_safe:
            break
    return is_safe


data = read_reports('data.txt')
results = list(map(lambda r: analyze_dampened(r), data))
print(sum(results))
