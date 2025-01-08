import heapq

def extract_from_file() -> list[list[str]]:
    with open("Day 20\\input.txt") as file:
        return [list(line.strip()) for line in file]

def find_start_end(racetrack: list[list[str]]) -> tuple[tuple[int, int], tuple[int, int]]:
    for i in range(len(racetrack)):
        for j in range(len(racetrack[i])):
            if racetrack[i][j] == "S":
                start = (i, j)
            elif racetrack[i][j] == "E":
                end = (i, j)
    return start, end

def find_path(racetrack: list[list[str]]) -> dict[tuple[int, int], int]:
    start, end = find_start_end(racetrack)
    directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]
    q = []
    heapq.heappush(q, (start[0], start[1], 0, dict())) # x, y, path length, visited dict: (x, y) -> path length

    while q:
        x, y , path_length, visited = heapq.heappop(q)

        if (x, y) in visited:
            continue
        visited[(x, y)] = path_length

        if (x, y) == end:
            break

        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if nx in range(len(racetrack)) and ny in range(len(racetrack[nx])) and racetrack[nx][ny] != "#":
                heapq.heappush(q, (nx, ny, path_length + 1, visited.copy()))
    
    return visited

def cheats_2_picoseconds(visited: dict[tuple[int, int], int]) -> dict[int, int]:
    cheats = dict() # time saved -> number of cheats
    for (a, b), l in visited.items():
        for i, j in [(a+2, b), (a-2, b), (a, b-2), (a, b+2)]:
            time_saved = visited.get((i, j), 0) - l - 2
            if time_saved > 0:
                cheats[time_saved] = cheats.get(time_saved, 0) + 1
    
    return cheats

def cheats_20_picoseconds(visited: dict[tuple[int, int], int]) -> dict[int, int]:
    cheats = dict() # time saved -> number of cheats
    path = sorted(visited, key=visited.get)
    for t2 in range(100, len(path)):
        for t1 in range(t2 - 100):
            x1, y1 = path[t1]
            x2, y2 = path[t2]
            dist = abs(x1 - x2) + abs(y1 - y2)
            time_saved = t2 - t1 - dist
            if time_saved > 0 and dist <= 20:
                cheats[time_saved] = cheats.get(time_saved, 0) + 1
    
    return cheats

def find_cheats_over_100(cheats: dict[int, int]) -> int:
    s = 0
    for time_saved, number_of_cheats in cheats.items():
        if time_saved >= 100:
            s += number_of_cheats
    
    return s

if __name__ == "__main__":
    racetrack = extract_from_file()
    vis = find_path(racetrack)
    cheats_2_picosecs = cheats_2_picoseconds(vis)
    cheats_20_picosecs = cheats_20_picoseconds(vis)

    print("Number of cheats of 2 picoseconds saving at least 100 picoseconds: ", find_cheats_over_100(cheats_2_picosecs))
    print("Number of cheats of 20 picoseconds saving at least 100 picoseconds: ", find_cheats_over_100(cheats_20_picosecs))