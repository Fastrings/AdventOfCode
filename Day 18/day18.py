from copy import deepcopy
import heapq

def extract_from_file() -> list[tuple[int, int]]:
    with open("Day 18\\input.txt") as file:
        return [(int(line.strip().split(',')[0]), int(line.strip().split(',')[1])) for line in file]

def find_path(bytes: list[tuple[int, int]], limit: int) -> int:
    directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]
    priority_queue = []
    heapq.heappush(priority_queue, (0, 0, 0))
    visited = set()
    blocks = set(bytes[:limit])

    while priority_queue:
        cost, x, y = heapq.heappop(priority_queue)

        if y == 70 and x == 70:
            return cost
        
        if (x, y) in visited:
            continue
        visited.add((x, y))

        for dx, dy in directions:
            new_x, new_y = x + dx, y + dy
            if (new_x, new_y) not in visited and (new_x, new_y) not in blocks and 0 <= new_x < 71 and 0 <= new_y < 71:
                heapq.heappush(priority_queue, (cost + 1, new_x, new_y))
    
    return -1

def find_first_blocking_byte(bytes: list[tuple[int, int]]) -> tuple[int, int]:
    left, right = 1024, len(bytes)
    while left < right - 1:
        mid = (left + right) // 2
        if find_path(bytes, mid) != -1:
            left = mid
        else:
            right = mid - 1
    
    return bytes[left]

if __name__ == '__main__':
    bytes = extract_from_file()
    print("Minimum number of steps to reach the bottom right corner: ", find_path(bytes, 1024))
    print("First blocking byte is at position: ", find_first_blocking_byte(bytes)) 