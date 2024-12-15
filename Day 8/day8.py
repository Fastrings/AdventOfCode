def extract_from_file():
    m = []
    with open("Day 8\\input.txt") as file:
        line = file.readline()
        while line:
            m.append(list(line.replace('\n', '')))
            line = file.readline()
    
    return m

def is_in_bounds(x: int, y: int) -> bool:
    return x in range(50) and y in range(50)

def find_another(position: tuple[int, int], antenna: str, grid: list[list[StopIteration]]) -> tuple[int, int]:
    x, y = position
    for i in range(x, 50):
        start_col = y + 1 if i == x else 0
        for j in range(start_col, 50):
            if grid[i][j] == antenna:
                return (i, j)
    return (-1, -1)

def find_antinodes() -> list[tuple[int, int]]:
    ant = set()
    grid = extract_from_file()
    for i in range(50):
        for j in range(50):
            if grid[i][j] == '.' or grid[i][j] == '#':
                continue
            
            another = find_another((i, j), grid[i][j], grid)
            while another != (-1, -1):
                another_x, another_y = another
                dx, dy = another_x - i, another_y - j
                if is_in_bounds(another_x + dx, another_y + dy):
                    ant.add((another_x + dx, another_y + dy))
                if is_in_bounds(i - dx, j - dy):
                    ant.add((i - dx, j - dy))
                another = find_another((another_x, another_y), grid[i][j], grid)

    return ant

def find_antinodes_with_resonant_harmonics() -> list[tuple[int, int]]:
    ant = set()
    grid = extract_from_file()
    for i in range(50):
        for j in range(50):
            if grid[i][j] == '.' or grid[i][j] == '#':
                continue
            
            ant.add((i, j))
            another = find_another((i, j), grid[i][j], grid)
            while another != (-1, -1):
                another_x, another_y = another
                dx, dy = another_x - i, another_y - j
                temp_i, temp_j = i, j
                temp_another_x, temp_another_y = another_x, another_y
                while is_in_bounds(temp_another_x + dx, temp_another_y + dy):
                    ant.add((temp_another_x + dx, temp_another_y + dy))
                    temp_another_x += dx
                    temp_another_y += dy
                while is_in_bounds(temp_i - dx, temp_j - dy):
                    ant.add((temp_i - dx, temp_j - dy))
                    temp_i -= dx
                    temp_j -= dy
                another = find_another((another_x, another_y), grid[i][j], grid)
    
    return ant

if __name__ == "__main__":
    print("Number of antinodes:", len(find_antinodes()))
    print("Number of antinodes with resonant harmonics: ", len(find_antinodes_with_resonant_harmonics()))