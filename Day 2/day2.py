def extract_from_file():
    reports = []
    with open("Day 2\\input.txt", "r") as file:
        line = file.readline()
        while line:
            line = list(map(lambda x: int(x), line.split()))
            reports.append(line)
            line = file.readline()

    return reports

def is_report_safe(report):
    differences = [report[i+1] - report[i] for i in range(len(report) - 1)]
    
    if all(1 <= diff <= 3 for diff in differences):
        return True
    
    if all(-3 <= diff <= -1 for diff in differences):
        return True
    
    return False

def is_report_safe_with_dampener(report):
    if is_report_safe(report):
        return True

    for i in range(len(report)):
        modified_list = report[:i] + report[i+1:]
        if is_report_safe(modified_list):
            return True

    return False

def report_safety_no_dampener():
    reports = extract_from_file()
    counter = 0
    for r in reports:
        if is_report_safe(r):
            counter += 1

    return counter

def report_safety_dampener():
    reports = extract_from_file()
    counter = 0
    for r in reports:
        if is_report_safe_with_dampener(r):
            counter += 1
    
    return counter

if __name__ == "__main__":
    print("Number of safe reports without the dampener: ", report_safety_no_dampener())
    print("Number of safe reports with the dampener: ", report_safety_dampener())