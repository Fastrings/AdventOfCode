def extract_from_file() -> tuple[list[tuple[int, int]], list[list[int]]]:
    contents = []
    with open("Day 5\\input.txt") as file:
        line = file.readline()
        while line:
            contents.append(line)
            line = file.readline()
    
    sep = contents.index('\n')
    rules: list[str] = contents[:sep]
    updates: list[str] = contents[sep + 1:]
    rules_clean, updates_clean = [], []
    for r in rules:
        temp = r.replace('\n', '').split('|')
        left = int(temp[0])
        right = int(temp[1])
        rules_clean.append((left, right))
    
    for u in updates:
        temp = u.replace('\n', '').split(',')
        temp = list(map(lambda x: int(x), temp))
        updates_clean.append(temp)

    return rules_clean, updates_clean

def is_update_correct(update: list[int], rules: tuple[int, int]) -> bool:
    for rule in rules:
        if rule[0] not in update or rule[1] not in update:
            continue
        if update.index(rule[0]) > update.index(rule[1]):
            return False
    
    return True

def sort_updates(rules: tuple[int, int], updates: list[list[int]]) -> list[list[int]]:
    correct_updates, incorrect_updates = [], []
    for update in updates:
        if is_update_correct(update, rules):
            correct_updates.append(update)
        else:
            incorrect_updates.append(update)
    
    return correct_updates, incorrect_updates

def fix_incorrect_updates(updates: list[list[int]], rules: tuple[int, int]) -> None:
    for update in updates:
        while not is_update_correct(update, rules):
            for rule in rules:
                if rule[0] not in update or rule[1] not in update:
                    continue
                left_i, right_i = update.index(rule[0]), update.index(rule[1])
                if left_i > right_i:
                    update[right_i], update[left_i] = update[left_i], update[right_i]          

def sum_of_middle_elements(updates: list[list[int]]) -> int:
    total = 0
    for u in updates:
        total += u[len(u) // 2]
    
    return total

if __name__ == "__main__":
    rules, updates = extract_from_file()
    corr, incorr = sort_updates(rules, updates)
    fix_incorrect_updates(incorr, rules)
    print("Sum of middle elements of initially correct lists of updates: ", sum_of_middle_elements(corr))
    print("Sum of middle elements of initially incorrect lists of updates: ", sum_of_middle_elements(incorr))