def extract_from_file() -> list[list[str]]:
    plots = []
    with open("Day 12\\input.txt") as file:
        line = file.readline()
        while line:
            plots.append(list(line.strip()))
            line = file.readline()
    
    return plots

def is_in_bounds(x: int, y: int, garden: list[list[str]]) -> bool:
    h, w = len(garden), len(garden[0])
    return x in range(h) and y in range(w)

def find_area(garden: list[list[str]], start_position: tuple[int, int]) -> list[tuple[int, int]]:
    area = []
    area_key = garden[start_position[0]][start_position[1]]
    visited = set()
    stack = [(start_position[0], start_position[1])]

    while stack:
        x, y = stack.pop()
        if (x, y) in visited:
            continue

        visited.add((x, y))
        if garden[x][y] == area_key:
            area.append((x, y))
        
        for dx, dy in [(-1, 0), (0, 1), (1, 0), (0, -1)]: # UP, RIGHT, DOWN, LEFT
            new_x, new_y = x + dx, y + dy
            if is_in_bounds(new_x, new_y, garden) and garden[new_x][new_y] == area_key:
                stack.append((new_x, new_y))
    
    return area

def find_perimeter(garden: list[list[str]], region_positions: list[tuple[int, int]]) -> int:
    perimeter = 0
    for pos in region_positions:
        x, y = pos
        key = garden[x][y]
        for dx, dy in [(-1, 0), (0, 1), (1, 0), (0, -1)]: # UP, RIGHT, DOWN, LEFT
            new_x, new_y = x + dx, y + dy
            if not is_in_bounds(new_x, new_y, garden) or garden[new_x][new_y] != key:
                perimeter += 1
    return perimeter

def find_number_of_sides(garden: list[list[str]], region_positions: list[tuple[int, int]]) -> int:
    if len(region_positions) in (1, 2):
        return 4
    
    corners = 0

    for pos in region_positions:
        (x, y) = pos
        key = garden[x][y]
        up = ' ' if not is_in_bounds(x - 1, y, garden) else garden[x - 1][y]
        right = ' ' if not is_in_bounds(x, y + 1, garden) else garden[x][y + 1]
        down = ' ' if not is_in_bounds(x + 1, y, garden) else garden[x + 1][y]
        left = ' ' if not is_in_bounds(x, y - 1, garden) else garden[x][y - 1]

        nw = ' ' if not is_in_bounds(x - 1, y - 1, garden) else garden[x - 1][y - 1]
        ne = ' ' if not is_in_bounds(x - 1, y + 1, garden) else garden[x - 1][y + 1]
        se = ' ' if not is_in_bounds(x + 1, y + 1, garden) else garden[x + 1][y + 1]
        sw = ' ' if not is_in_bounds(x + 1, y - 1, garden) else garden[x + 1][y - 1]
        # corners
        if up != key and right != key:
            corners += 1
        if right != key and down != key:
            corners += 1
        if down != key and left != key:
            corners += 1
        if left != key and up != key:
            corners += 1
        
        # negative corners
        if nw != key and up == key and left == key: # NW
            corners += 1
        if ne != key and up == key and right == key: # NE
            corners += 1
        if se != key and down == key and right == key: # SE
            corners += 1
        if sw != key and down == key and left == key: # SW
            corners += 1

    return corners

def compute_total_price_of_fences(garden: list[list[str]]) -> tuple[int, int]:
    h, w = len(garden), len(garden[0])
    visited = set()
    total_price = 0
    total_price_discount = 0
    for i in range(h):
        for j in range(w):
            key = garden[i][j]
            if (i, j, key) in visited:
                continue
            
            area_positions = find_area(garden, (i, j))
            for pos in area_positions:
                x, y = pos
                visited.add((x, y, key))
            
            perimeter = find_perimeter(garden, area_positions)
            num_of_sides = find_number_of_sides(garden, area_positions)
            total_price += len(area_positions) * perimeter
            total_price_discount += len(area_positions) * num_of_sides
            # for debugging, print area symbol + area + perimeter
            #print(f"'{key}' ---> area = {len(area_positions)}, perimeter = {perimeter}, number of sides = {num_of_sides}")
    
    return total_price, total_price_discount

if __name__ == "__main__":
    garden = extract_from_file()
    price, price_discount = compute_total_price_of_fences(garden)
    print("Total price of fence for this garden: ", price)
    print("Discounted price of fence for this garden: ", price_discount)