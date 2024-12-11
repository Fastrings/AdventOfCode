import re

def extract_from_file():
    with open("Day 3\\input.txt") as file:
        txt = file.read()
    
    return txt

def find_all_matches(txt):
    regex1 = r"mul\(\d{1,3},\d{1,3}\)"
    regex2 = r"mul\(\d{1,3},\d{1,3}\)|do\(\)|don't\(\)"
    matches1 = re.findall(regex1, txt)
    matches2 = re.findall(regex2, txt)
    return matches1, matches2

def compute(str: str):
    newstr = str.replace('(', '').replace(')', '')[3:]
    left = newstr.split(',')[0]
    right = newstr.split(',')[1]

    return int(left) * int(right)

if __name__ == "__main__":
    txt = extract_from_file()
    matches1, matches2 = find_all_matches(txt)
    total1, total2 = 0, 0
    for m in matches1:
        total1 += compute(m)
    
    flag = True
    for m in matches2:
        if m == "do()":
            flag = True
            continue
        elif m == "don't()":
            flag = False
            continue

        if flag:
            total2 += compute(m)
    
    print(total1)
    print(total2)