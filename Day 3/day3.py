import re

def extract_from_file() -> str:
    with open("Day 3\\input.txt") as file:
        txt = file.read()
    
    return txt

def find_all_matches(txt: str) -> tuple[list, list]:
    regex1 = r"mul\(\d{1,3},\d{1,3}\)"
    regex2 = r"mul\(\d{1,3},\d{1,3}\)|do\(\)|don't\(\)"
    matches1 = re.findall(regex1, txt)
    matches2 = re.findall(regex2, txt)
    return matches1, matches2

def compute(str: str) -> int:
    newstr = str.replace('(', '').replace(')', '')[3:]
    left = newstr.split(',')[0]
    right = newstr.split(',')[1]

    return int(left) * int(right)

def sum_of_mult(txt: str) -> int:
    matches = find_all_matches(txt)[0]
    total = 0
    for m in matches:
        total += compute(m)
    return total

def sum_of_mult_enabled(txt: str) -> int:
    matches = find_all_matches(txt)[1]
    total = 0
    flag = True
    for m in matches:
        if m == "do()":
            flag = True
            continue
        elif m == "don't()":
            flag = False
            continue

        if flag:
            total += compute(m)
    
    return total

if __name__ == "__main__":
    print("Sum of multiplications: ", sum_of_mult(extract_from_file()))
    print("Sum of enabled multiplications: ", sum_of_mult_enabled(extract_from_file()))