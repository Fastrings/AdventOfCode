def extract_from_file() -> list[list[int]]:
    m = []
    with open("Day 10\\input.txt") as file:
        line = file.readline()
        while line:
            m.append(list(map(lambda x: int(x), line.replace('\n', ''))))
            line = file.readline()
    
    return m

def is_in_bounds(x: int, y: int, m:list[list[int]]) -> bool:
    h, w = len(m), len(m[0])
    return x in range(h) and y in range(w)

def count_reachable_summits(topomap: list[list[int]], start_position: tuple[int, int]) -> int:
    visited = set()
    score = 0
    startx, starty = start_position
    stack = [(startx, starty, 0)]

    while stack:
        x, y, l = stack.pop()
        if (x, y) in visited:
            continue

        visited.add((x, y))
        if topomap[x][y] == 9 and l == 9:
            score += 1
        
        for dx, dy in [(-1, 0), (0, 1), (1, 0), (0, -1)]: # UP, RIGHT, DOWN, LEFT
            nx, ny = x + dx, y + dy
            if is_in_bounds(nx, ny, topomap) and (nx, ny) not in visited and topomap[nx][ny] == l + 1:
                stack.append((nx, ny, l + 1))
    
    return score

def compute_rating(topomap: list[list[int]], start_position: tuple[int, int]) -> int:
    rating = 0 # total number of paths
    startx, starty = start_position
    stack = [(startx, starty, set(), 0)]

    while stack:
        x, y, visited, l = stack.pop()
        visited.add((x, y))

        if topomap[x][y] == 9 and l == 9:
            rating += 1
        else:
            for dx, dy in [(-1, 0), (0, 1), (1, 0), (0, -1)]: # UP, RIGHT, DOWN, LEFT
                nx, ny = x + dx, y + dy
                if is_in_bounds(nx, ny, topomap) and (nx, ny) not in visited and topomap[nx][ny] == l + 1:
                    stack.append((nx, ny, visited.copy(), l + 1))
        
        visited.remove((x, y))
    
    return rating

def sum_of_scores(topomap: list[list[int]]) -> int:
    h, w = len(topomap), len(topomap[0])
    total_score = 0
    total_rating = 0
    for i in range(h):
        for j in range(w):
            if topomap[i][j] == 0:
                score = count_reachable_summits(topomap, (i, j))
                rating = compute_rating(topomap, (i,  j))
                total_score += score
                total_rating += rating
    
    return total_score, total_rating
                

if __name__ == "__main__":
    topomap = extract_from_file()
    total_score, total_rating = sum_of_scores(topomap)
    print("Sum of trailhead scores of topographic map:", total_score)
    print("Sum of trailhead ratings of topographic map:", total_rating)