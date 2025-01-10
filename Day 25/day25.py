type grid = list[list[str]]

def extract_from_file() -> list[grid]:
    grids = []
    with open("Day 25\\input.txt") as file:
        lines = file.readlines()
        curr_grid = []
        for l in lines:
            if l == '\n':
                grids.append(curr_grid)
                curr_grid = []
                continue

            curr_grid.append(list(l.strip()))

    grids.append(curr_grid)
    return grids

def grid_to_heights(grid: grid) -> tuple[str, list[int]]:
    transpose = [[grid[j][i] for j in range(len(grid))] for i in range(len(grid[0]))]
    heights = []
    height_type = "LOCK" if transpose[0][0] == '#' else "KEY"
    for line in transpose:
        joined = ''.join(line)
        height = joined.count('#') - 1
        heights.append(height)
    
    return (height_type, heights)

def is_fitting(key_heights: list[int], lock_heights: list[int]) -> bool:
    return all([x + y <= 5 for x, y in zip(key_heights, lock_heights)])

def find_non_overlapping(grids: list[grid]) -> int:
    pairs_non_overlap = set()
    heights = [grid_to_heights(g) for g in grids]
    keys = [h for h in heights if h[0] == "KEY"]
    locks = [h for h in heights if h[0] == "LOCK"]

    for lock in locks:
        lock_heights = lock[1]
        for key in keys:
            key_heights = key[1]
            if is_fitting(key_heights, lock_heights):
                l = ("LOCK", int(''.join(map(str, lock_heights)))) # change list[int] -> int to be hashable
                k = ("KEY", int(''.join(map(str, key_heights)))) # change list[int] -> int to be hashable
                pairs_non_overlap.add((l, k))
    
    return len(pairs_non_overlap)

if __name__ == '__main__':
    grids = extract_from_file()
    print("Number of unique key/lock pairs without any overlap: ", find_non_overlapping(grids))