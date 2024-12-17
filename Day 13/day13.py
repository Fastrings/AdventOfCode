import re

type Machine = tuple[tuple[int, int], tuple[int, int], tuple[int, int]]

BIG_NUM = 10_000_000_000_000

def extract_from_file() -> list[Machine]:
    machines = []
    with open("Day 13\\input.txt") as file:
        line = file.readline()
        while line:
            line = line.strip()
            if line != '':
                nums = re.findall(r'\d+', line)
                x, y = int(nums[0]), int(nums[1])
                machines.append((x, y))
            line = file.readline()


    machines = [tuple(machines[i:i + 3]) for i in range(0, len(machines), 3)]
    return machines

def button_presses_to_get_prize(machine: Machine, offset: int = 0) -> tuple[int, int]:
    (adx, ady), (bdx, bdy), (prize_x, prize_y) = machine
    tolerance = 0.0001
    prize_x += offset
    prize_y += offset
    A = (bdx * prize_y - bdy * prize_x) / (bdx * ady - bdy * adx)
    B = (prize_x - adx * A) / bdx

    if abs(A - round(A)) >= tolerance or abs(B - round(B)) >= tolerance:
            return 0, 0
    
    return A, B

def sum_of_tokens(machines: list[Machine], offset: int = 0) -> int:
    total_num_of_tokens = 0
    for m in machines:
        button_a_presses, button_b_presses = button_presses_to_get_prize(m, offset)
        #print("- ", button_a_presses, ", ", button_b_presses, " -")
        token_cost = 3 * button_a_presses + button_b_presses
        total_num_of_tokens += token_cost
        #print("---", token_cost, "---")
    
    return total_num_of_tokens

if __name__ == "__main__":
    machines = extract_from_file()
    print("Fewest number of tokens needed to get every prize: ", sum_of_tokens(machines))
    print("Fewest number of tokens needed to get every prize with big offset: ", sum_of_tokens(machines, offset=BIG_NUM))