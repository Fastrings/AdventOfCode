from itertools import product

def extract_from_file():
    d = {}
    with open("Day 7\\input.txt") as file:
        line = file.readline()
        while line:
            line = line.replace('\n', '').split(':')
            left, right = int(line[0]), line[1]
            d[left] = list(map(lambda x: int(x), right.split(' ')[1:]))
            line = file.readline()
        
        return d

def compute_expression(numbers: list[int], operators: list[str]) -> int:
    res = numbers[0]
    for i, op in enumerate(operators):
        if op == '+':
            res += numbers[i + 1]
        elif op == '*':
            res *= numbers[i + 1]
        elif op == '||':
            res = int(str(res) + str(numbers[i + 1]))
    
    return res

def is_expression_correct(numbers: list[int], total: int, operator_combinations: product) -> bool:
    for combi in operator_combinations:
        if compute_expression(numbers, combi) == total:
            return True
    return False

def sum_of_expressions():
    di = extract_from_file()
    s1, s2 = 0, 0
    for total, exp in di.items():
        if is_expression_correct(exp, total, product(['+', '*'], repeat=len(exp) - 1)):
            s1 += total
        elif is_expression_correct(exp, total, product(['+', '*', '||'], repeat=len(exp) - 1)):
            s2 += total
    
    return s1, s2

if __name__ == "__main__":
    sum1, sum2 = sum_of_expressions()
    print("Number of totals of correct expressions: ", sum1)
    print("Number of totals of correct expressions when adding || operator: ", sum1 + sum2)