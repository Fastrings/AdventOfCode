import re, time

type Robot = tuple[tuple[int, int], tuple[int, int]]

def extract_from_file() -> list[Robot]:
    robots = []
    with open("Day 14\\input.txt") as file:
        line = file.readline().strip()
        while line:
            nums = re.findall(r'-?\d+', line)
            pos_x, pos_y, vel_x, vel_y = map(int, nums)
            robots.append(((pos_x, pos_y), (vel_x, vel_y)))
            line = file.readline()
        
    return robots

def move_robots(robots: list[Robot], seconds: int) -> list[tuple[int, int]]:
    new_robots_positions = []
    for robot in robots:
        position, velocity = robot
        pos_x, pos_y = position
        vel_x, vel_y = velocity
        new_pos_x = (pos_x + vel_x * seconds) % 101
        new_pos_y = (pos_y + vel_y * seconds) % 103
        new_robots_positions.append((new_pos_x, new_pos_y))

    return new_robots_positions

def count_quadrants(robots: list[Robot], seconds: int) -> int:
    positions = move_robots(robots, seconds)
    NE, SE, SW, NW = 0, 0, 0, 0
    for pos in positions:
        x, y = pos
        if x == 50 or y == 51: # In the middle = not in any quadrant
            continue
        elif x > 50 and y < 51: # Top right quadrant
            NE += 1
        elif x > 50 and y > 51: # Bottom right quadrant
            SE += 1
        elif x < 50 and y > 51: # Bottom left quadrant
            SW += 1
        elif x < 50 and y < 51: # Top left quadrant
            NW += 1
        else:
            raise Exception("We done goofed")
        
    #print(f"{NE} * {SE} * {SW} * {NW} = {NE * SE * SW * NW}")
    
    return NE * SE * SW * NW

def seconds_to_reach_easter_egg(robots: list[Robot]) -> int:
    seconds = 0
    while True:
        positions = []
        seconds += 1
        is_christmas_tree = False

        for robot in robots:
            position, velocity = robot
            pos_x, pos_y = position
            vel_x, vel_y = velocity
            new_pos_x = (pos_x + vel_x * seconds) % 101
            new_pos_y = (pos_y + vel_y * seconds) % 103
            positions.append((new_pos_x, new_pos_y))
            if positions.index((new_pos_x, new_pos_y)) != len(positions) - 1:
                is_christmas_tree = True

        if not is_christmas_tree:
            return seconds

if __name__ == "__main__":
    robots = extract_from_file()
    print("Safety factor after 100 seconds: ", count_quadrants(robots, 100))
    print("Number of seconds needed to display easter egg: ", seconds_to_reach_easter_egg(robots))