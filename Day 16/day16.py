import heapq

def extract_from_file() -> list[list[str]]:
    with open("Day 16\\input.txt") as file:
        return [list(line.strip()) for line in file]

def init_locations(racemap: list[list[str]]) -> tuple[tuple[int, int], tuple[int, int]]:
    end = start = -1, -1
    height, width = len(racemap), len(racemap[0])
    for i in range(height):
        for j in range(width):
            if racemap[i][j] == 'S':
                start = i, j
            elif racemap[i][j] == 'E':
                end = i, j
    
    return start, end

def is_in_bounds(x: int, y: int, racemap: list[list[str]]) -> bool:
    height, width = len(racemap), len(racemap[0])
    return x in range(height) and y in range(width)

def cost_shortest_path(racemap: list[list[str]], start: tuple[int, int], end: tuple[int, int]) -> int:
    directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]
    priority_queue = []
    heapq.heappush(priority_queue, (0, start[0], start[1], 1))
    visited = set()

    while priority_queue:
        cost, x, y, direction = heapq.heappop(priority_queue)

        if (x, y) == end: # Found the end, return the cost
            return cost
        
        if (x, y, direction) in visited: # Already visited this location, skip
            continue
        visited.add((x, y, direction))

        dx, dy = directions[direction] # Moving forward in the current direction
        new_x, new_y = x + dx, y + dy
        if is_in_bounds(new_x, new_y, racemap) and racemap[new_x][new_y] != '#':
            heapq.heappush(priority_queue, (cost + 1, new_x, new_y, direction))
        
        new_direction_counterclockwise = (direction - 1) % 4 # Rotating left
        if is_in_bounds(x, y, racemap) and racemap[x][y] != '#':
            heapq.heappush(priority_queue, (cost + 1000, x, y, new_direction_counterclockwise))

        new_direction_clockwise = (direction + 1) % 4 # Rotating right
        if is_in_bounds(x, y, racemap) and racemap[x][y] != '#':
            heapq.heappush(priority_queue, (cost + 1000, x, y, new_direction_clockwise))
    
    return -1 # No path found

def find_possible_seats(racemap: list[list[str]], start: tuple[int, int], end: tuple[int, int]) -> int:
    directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]
    priority_queue = []
    heapq.heappush(priority_queue, (0, start[0], start[1], 1, [start]))
    paths = []
    best_cost = float('inf')
    visited = {}

    while priority_queue and priority_queue[0][0] <= best_cost:
        cost, x, y, direction, path = heapq.heappop(priority_queue)

        if (x, y) == end: # Found the end, return the cost
            best_cost = cost
            paths.append(path)
            continue
        
        if (x, y, direction) in visited and visited[(x, y, direction)] < cost:
            continue
        visited[(x, y, direction)] = cost

        dx, dy = directions[direction] # Moving forward in the current direction
        new_x, new_y = x + dx, y + dy
        if is_in_bounds(new_x, new_y, racemap) and racemap[new_x][new_y] != '#' and (new_x, new_y) not in path:
            heapq.heappush(priority_queue, (cost + 1, new_x, new_y, direction, path + [(new_x, new_y)]))
        
        new_direction_counterclockwise = (direction - 1) % 4 # Rotating left
        if is_in_bounds(x, y, racemap) and racemap[x][y] != '#':
            heapq.heappush(priority_queue, (cost + 1000, x, y, new_direction_counterclockwise, path))

        new_direction_clockwise = (direction + 1) % 4 # Rotating right
        if is_in_bounds(x, y, racemap) and racemap[x][y] != '#':
            heapq.heappush(priority_queue, (cost + 1000, x, y, new_direction_clockwise, path))
    
    seats = set()
    for path in paths:
        seats |= set(path)
    
    return len(seats)

if __name__ == '__main__':
    racemap = extract_from_file()
    start, end = init_locations(racemap)
    cost = cost_shortest_path(racemap, start, end)
    seats = find_possible_seats(racemap, start, end)
    print("Lowest score of reindeer: ", cost)
    print("Number of tiles that are at least in one of the best paths: ", seats)