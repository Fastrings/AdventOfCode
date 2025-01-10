"""
DISCLAIMER:

This is not my solution, I spent too much time on this problem.
All credit goes to this blog post: https://winslowjosiah.com/blog/2024/12/16/advent-of-code-2024-day-15/

"""

from collections import defaultdict, deque
from typing import TypeAlias

Grid: TypeAlias = defaultdict[complex, str]
OFFSETS: dict[str, complex] = {
    ">": 1 + 0j, "<": -1 + 0j, "v": 1j, "^": -1j,
}
WIDE_TILES = {".": "..", "#": "##", "O": "[]"}

def extract_from_file() -> list[str]:
    with open("Day 15\\input.txt") as file:
        return [line.strip() for line in file.readlines()]

def sum_of_GPS_coords_small_map(lines: list[str]) -> int:
    grid = defaultdict(lambda: '#')
    robot = None
    lines_iter = iter(lines)

    for y, row in enumerate(lines_iter):
        if not row:
            break # We have reached the end of the grid
        for x , tile in enumerate(row):
            position = x + y * 1j
            if tile == '@':
                robot, tile = position, '.'
            grid[position] = tile
    
    moves = ''.join(lines_iter)

    for move in moves:
        offset = OFFSETS.get(move, 0j)
        new_robot = robot + offset
        new_robot_tile = grid[new_robot]

        if new_robot_tile == '#':
            continue
        elif new_robot_tile == 'O':
            box = new_robot
            while (tile := grid[box]) == 'O':
                box += offset
            
            if tile == '#':
                continue
            
            grid[box], grid[new_robot] = grid[new_robot], tile
        
        robot = new_robot
    
    return sum([100 * int(pos.imag) + int(pos.real) for pos, tile in grid.items() if tile == 'O'])

def sum_of_GPS_coords_big_map(lines: list[str]) -> int:
    WIDE_BOX = WIDE_TILES['O']
    lines_iter = iter(lines)
    grid = defaultdict(lambda: "#")
    robot = None

    for y, row in enumerate(lines_iter):
        if not row:
            break

        for x, tile in enumerate(row):
            position = x * 2 + y * 1j
            if tile == '@':
                robot, tile = position, '.'
            for w, wide_tile in enumerate(WIDE_TILES.get(tile, WIDE_TILES["."])):
                grid[position + w] = wide_tile
    
    moves = ''.join(lines_iter)

    for move in moves:
        offset = OFFSETS.get(move, 0j)
        new_robot = robot + offset
        new_robot_tile = grid[new_robot]
        robot_is_pushing = new_robot_tile in WIDE_BOX

        if new_robot_tile == '#':
            continue
        elif robot_is_pushing and move in '<>':
            box = new_robot
            while (tile := grid[box]) in WIDE_BOX:
                box += offset
            if tile == "#":
                continue

            while box != new_robot:
                grid[box] = grid[box - offset]
                box -= offset
            grid[new_robot] = tile
        elif robot_is_pushing and move in '^v':
            boxes_to_push = {}
            box = new_robot
            while grid[box] != WIDE_BOX[0]:
                box -= 1
            box_queue = deque([box])

            while box_queue:
                box = box_queue.popleft()
                boxes_to_push[box] = None
                for w in range(len(WIDE_BOX)):
                    in_front = box + w + offset
                    if grid[in_front] == '#':
                        box_queue.clear()
                        boxes_to_push.clear()
                        break
                    elif grid[in_front] in WIDE_BOX:
                        while grid[in_front] != WIDE_BOX[0]:
                            in_front -= 1
                        boxes_to_push[in_front] = None
                        box_queue.append(in_front)
            
            if not boxes_to_push:
                continue

            for box in reversed(boxes_to_push):
                for w in range(len(WIDE_BOX)):
                    grid[box + w + offset], grid[box + w] = grid[box + w], grid[box + w + offset]
        
        robot = new_robot
    
    return sum([100 * int(pos.imag) + int(pos.real) for pos, char in grid.items() if char == WIDE_BOX[0]])

if __name__ == "__main__":
    lines = extract_from_file()
    print("Sum of GPS coordinates on the small map: ", sum_of_GPS_coords_small_map(lines))
    print("Sum of GPS coordinates on the scaled up map: ", sum_of_GPS_coords_big_map(lines))