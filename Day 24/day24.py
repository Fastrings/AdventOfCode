from collections import defaultdict

def extract_from_file() -> tuple[dict[str: int], list[tuple[str, str, str, str]]]:
    d = {}
    assignments = []
    with open("Day 24\\input.txt") as file:
        line = file.readline()
        while line:
            line = line.strip()
            if ':' in line:
                left = line[:3]
                right = int(line[-1])
                d[left] = right
            elif '->' in line:
                inputs, output = line.split(" -> ")
                input_left, operator, input_right = inputs.split(" ")
                assignments.append((input_left, operator, input_right, output))
        
            line = file.readline()
    
    return d, assignments

def process(left: int, right: int, op: str) -> str:
    match op:
        case "AND":
            return left & right
        case "XOR":
            return left ^ right
        case "OR":
            return left | right
        case _:
            raise Exception("We done goofed")

def assign_values(values: dict[str: int], assignments: list[tuple[str, str, str, str]]) -> dict[str: int]:
    available_inputs = set(values.keys())
    processed_outputs = set()
    number_of_ops = len(assignments)

    while len(processed_outputs) < number_of_ops:
        for (input_left, op, input_right, out) in assignments:
            if input_left in available_inputs or input_left in processed_outputs:
                if input_right in available_inputs or input_right in processed_outputs:
                    if out not in processed_outputs:
                        left = values[input_left]
                        right = values[input_right]
                        res = process(left, right, op)
                        values[out] = res
                        processed_outputs.add(out)
    
    return values

def find_swapped_operations(assignments: list[tuple[str, str, str, str]]) -> list[str]:
    d = defaultdict(set)
    swaps = []

    for (input_left, operator, input_right, _) in assignments:
        d[input_left].add(operator)
        d[input_right].add(operator)
    
    for (input_left, operator, input_right, output) in assignments:
        if output == "z45":  # Last operation for highest bit
            if input_left[0] in "xy" or input_right[0] in "xy" or operator != "OR":
                swaps.append(output)
            continue

        if output == "z00": # First operation for lowest bit
            if sorted([input_left, input_right]) != ["x00", "y00"] or operator != "XOR":
                swaps.append(output)
            continue

        if input_left in ["x00", "y00"] or input_right in ["x00", "y00"]: # Another special case for first operation
            if (input_left[0] == "x" and input_right[0] == "y") or (input_left[0] == "y" and input_right[0] == "x"):
                if operator == "OR":
                    swaps.append(output)
            continue

        match operator:
            case "AND": # If operator is AND: left has x or y and right has neither -> swap happened
                if input_left[0] in "xy" and input_right[0] not in "xy":
                    swaps.append(output)
                if "OR" not in d[output]:
                    swaps.append(output)
            case "OR": # If operator is OR: We dont want to see any x, y or z here -> if we do, swap happened
                if input_left[0] in "xy" or input_right[0] in "xy" or output[0] == "z":
                    swaps.append(output)
                if "AND" not in d[output] or "XOR" not in d[output]:
                    swaps.append(output)
            case "XOR":
                # If operator is XOR: If left or right have x or y -> swap happened if output has z. Otherwise swap happened if output doesnt have z
                if input_left[0] in "xy":
                    if input_right[0] not in "xy" or output[0] == 'z':
                        swaps.append(output)
                    if "AND" not in d[output] or "XOR" not in d[output]:
                        swaps.append(output)
                elif output[0] != "z":
                    swaps.append(output)
    
    return sorted(list(set(swaps)))

def compute_z_wires(values: dict[str: int]) -> int:
    total = 0
    for k, v in values.items():
        if k[0] == 'z':
            total += v * (2 ** int(k[1:]))

    return total

if __name__ == '__main__':
    values, assignments = extract_from_file()
    new_values = assign_values(values, assignments)
    print("Decimal number from wires starting with z: ", compute_z_wires(new_values))
    print("Names of wires involved in a swap: ", ','.join(find_swapped_operations(assignments)))