from functools import cache

NUMPAD = {
    '0': (3, 1),
    '1': (2, 0),
    '2': (2, 1),
    '3': (2, 2),
    '4': (1, 0),
    '5': (1, 1),
    '6': (1, 2),
    '7': (0, 0),
    '8': (0, 1),
    '9': (0, 2),
    'A': (3, 2)
}

DIRECTIONAL_PAD = {
    '^': (0, 1),
    '<': (1, 0),
    'v': (1, 1),
    '>': (1, 2),
    'A': (0, 2),
}

def extract_from_file() -> list[str]:
    with open ("Day 21\\input.txt") as file:
        return [line.strip() for line in file.readlines()]

def generate_paths(pad: dict[str: tuple[int, int]], forbidden: tuple[int, int]) -> dict[tuple[int, int]: str]:
    paths = {}
    for i, (x, y) in pad.items():
        for j, (x2, y2) in pad.items():
            path = '<' * (y - y2) +  'v' * (x2 - x) + '^' * (x - x2) + '>' * (y2 - y) # left first, then middle then right -> paths are shorter in the end
            if (x, y2) == forbidden or (x2, y) == forbidden:
                path = path[::-1] # ^> becomes >^ if we step on gap in keypad

            paths[(i, j)] = path + 'A'
    
    return paths

def convert_sequence(sequence: str, paths: dict[tuple[int, int]: str]) -> str:
    result = ''
    start = 'A'
    for s in sequence:
        result += paths[(start, s)]
        start = s
    
    return result

def compute_complexity(code: str) -> int:
    numpad_paths = generate_paths(NUMPAD, (3, 0))
    directional_paths = generate_paths(DIRECTIONAL_PAD, (3, 0))

    robot1_inst = convert_sequence(code, numpad_paths)
    robot2_inst = convert_sequence(robot1_inst, directional_paths)
    human_inst = convert_sequence(robot2_inst, directional_paths)

    left = len(human_inst)
    right = int(code[:-1])

    return left * right

@cache
def compute_length(sequence: str, iterations_left: int) -> int:
    directions_paths = generate_paths(DIRECTIONAL_PAD, (0, 0))
    if iterations_left == 0:
        return len(sequence)
    
    start = 'A'
    total_length = 0
    for s in sequence:
        total_length += compute_length(directions_paths[(start, s)], iterations_left - 1)
        start = s
    
    return total_length
    
def sum_of_complexities(codes: list[str]) -> int:
    return sum([compute_complexity(code) for code in codes])

def sum_of_complexities_25(codes: list[str]) -> int:
    numpad_paths = generate_paths(NUMPAD, (3, 0))
    total = 0
    for code in codes:
        to_convert = convert_sequence(code, numpad_paths) # 1 numpad
        total += compute_length(to_convert, 25) * int(code[:-1]) # 25 directional pads
    
    return total

if __name__ == '__main__':
    codes = extract_from_file()
    print("Sum of complexities after 2 directional pads and 1 numerical pad: ", sum_of_complexities(codes))
    print("Sum of complexities after 25 directional pads and 1 numerical pad: ", sum_of_complexities_25(codes))