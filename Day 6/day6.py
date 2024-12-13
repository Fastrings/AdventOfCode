DIRECTIONS = [(-1, 0), (0, 1), (1, 0), (0, -1)]

def extract_from_file() -> list[list[str]]:
    m = []
    with open("Day 6\\input.txt") as file:
        line = file.readline()
        while line:
            m.append(list(line.replace('\n', '')))
            line = file.readline()
    
    return m

def is_in_bounds(x: int, y: int) -> bool:
    return x in range(130) and y in range(130)

def visited_positions(facility_map: list[list[str]]) -> set:
    visited = set()
    directions_counter = 0
    di, dj = DIRECTIONS[0]
    i, j = 45, 42
    while is_in_bounds(i, j):
        visited.add((i, j))
        new_i, new_j = i + di, j + dj
        if not is_in_bounds(new_i, new_j):
            break

        while facility_map[new_i][new_j] == '#':
            directions_counter = (directions_counter + 1) % 4
            di, dj = DIRECTIONS[directions_counter]
            new_i, new_j = i + di, j + dj

        i, j = new_i, new_j
    
    return visited

def has_loop(directions_counter: int, obstacle_position: tuple[int, int], facility_map: list[list[str]]) -> bool:
    oi, oj = obstacle_position
    di, dj = DIRECTIONS[directions_counter]
    i, j = oi - di, oj - dj
    facility_map[oi][oj] = '#'
    visited = set()

    while is_in_bounds(i, j):
        if (i, j, directions_counter) in visited:
            facility_map[oi][oj] = '.'
            return True
        
        if facility_map[i][j] == '#':
            raise Exception("We done goofed")
        
        visited.add((i, j, directions_counter))
        new_i, new_j = i + di, j + dj
        if not is_in_bounds(new_i, new_j):
            break

        while facility_map[new_i][new_j] == '#':
            directions_counter = (directions_counter + 1) % 4
            di, dj = DIRECTIONS[directions_counter]
            new_i, new_j = i + di, j + dj

        i, j = new_i, new_j
    
    facility_map[oi][oj] = '.'
    return False

def find_all_possible_loops(facility_map: list[list[str]]) -> int:
    i, j = 45, 42
    directions_counter = 0
    di, dj = DIRECTIONS[0]
    visited = set()
    num_of_obstacles_that_make_loops = 0

    while is_in_bounds(i, j):
        visited.add((i, j))
        new_i, new_j = i + di, j + dj
        if not is_in_bounds(new_i, new_j):
            break

        while facility_map[new_i][new_j] == '#':
            directions_counter = (directions_counter + 1) % 4
            di, dj = DIRECTIONS[directions_counter]
            new_i, new_j = i + di, j + dj

        if (new_i, new_j) not in visited and has_loop(directions_counter, (new_i, new_j), facility_map):
            num_of_obstacles_that_make_loops += 1
        
        i, j = new_i, new_j
    
    return num_of_obstacles_that_make_loops

if __name__ == "__main__":
    facility_map = extract_from_file()
    print("Total visited steps: ", len(visited_positions(facility_map)))
    print("Number of possible obstacle placements: ", find_all_possible_loops(facility_map))