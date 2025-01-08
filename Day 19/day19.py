def extract_from_file() -> tuple[list[str], list[str]]:
    with open("Day 19\\input.txt") as f:
        lines = f.readlines()
    
    patterns = lines[0].strip().replace(' ', '').split(',')
    designs = list(map(lambda x: x.strip(), lines[2:]))
    return patterns, designs

def all_possible_constructions(design: str, patterns: list[str]) -> int:
    patterns_set = set(patterns)
    dp = [0] * (len(design) + 1)
    for i in range(1, len(design) + 1):
        for j in range(i):
            for pat in patterns_set:
                if j + len(pat) == i and pat == design[j:i]:
                    if j == 0:
                        dp[i] += 1
                    else:
                        dp[i] += dp[j]
    
    return dp[-1]

def count_possible_designs(patterns: list[str], designs: list[str]) -> int:
    number_of_possible_designs = 0
    number_of_total_constructions = 0
    for design in designs:
        const = all_possible_constructions(design, patterns)
        if const > 0:
            number_of_possible_designs += 1
            number_of_total_constructions += const
    
    return number_of_possible_designs, number_of_total_constructions

if __name__ == '__main__':
    patterns, designs = extract_from_file()
    possible_designs, total_constructions = count_possible_designs(patterns, designs)
    print("Number of possible designs:", possible_designs)
    print("Number of total constructions:", total_constructions)