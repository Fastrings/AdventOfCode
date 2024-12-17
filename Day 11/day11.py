from collections import Counter

def extract_from_file() -> Counter:
    with open("Day 11\\input.txt") as file:
        return Counter(map(int, file.read().split()))

def count_stones(stones: Counter, blinks: int) -> int:
    for _ in range(blinks):
        new_stones = Counter()
        for n, num_of_stones in stones.items():
            mid, remainder = divmod(len(str(n)), 2)
            if n == 0:
                new_stones[1] += num_of_stones
            elif remainder:
                new_stones[2024 * n] += num_of_stones
            else:
                for m in divmod(n, 10 ** mid):
                    new_stones[m] += num_of_stones
        stones = new_stones
    
    return sum(stones.values())

if __name__ == "__main__":
    stones = extract_from_file()
    print("Number of stones after 25 blinks: ", count_stones(stones, 25))
    print("Number of stones after 75 blinks: ", count_stones(stones, 75))