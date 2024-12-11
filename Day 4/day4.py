XMAS = 'XMAS'

directions = [
    (-1, 0), #north
    (0, 1), #east
    (1, 0), #south
    (0, -1), #west
    (-1, 1), #northeast
    (1, 1), #southeast
    (1, -1), #southwest
    (-1, -1), #northwest
]

def extract_from_file():
    m = []
    with open("Day 4\\input.txt") as file:
        line = file.readline()
        while line:
            m.append(list(line.replace('\n', '')))
            line = file.readline()
    
    return m

def is_in_bounds(x, y):
    return 0 <= x < 140 and 0 <= y < 140

def is_valid_occurence(x, y, dx, dy, m):
    for k in range(4):
        nx, ny = x + k * dx, y + k * dy
        if not is_in_bounds(nx, ny) or m[nx][ny] != XMAS[k]:
            return False
    return True

def count_xmas_occurences():
    m = extract_from_file()
    total_occurences = 0
    for i in range(140):
        for j in range(140):
            for dx, dy in directions:
                if is_valid_occurence(i, j, dx, dy, m):
                    total_occurences += 1
    
    return total_occurences

def is_valid_cross(x, y, m):
    #left to right
    if m[x - 1][y - 1] == 'M' and m[x + 1][y + 1] == 'S' and m[x + 1][y - 1] == 'M' and m[x - 1][y + 1] == 'S':
        return True
    #right to left
    if m[x - 1][y - 1] == 'S' and m[x + 1][y + 1] == 'M' and m[x + 1][y - 1] == 'S' and m[x - 1][y + 1] == 'M':
        return True
    #up to down
    if m[x - 1][y - 1] == 'M' and m[x + 1][y + 1] == 'S' and m[x + 1][y - 1] == 'S' and m[x - 1][y + 1] == 'M':
        return True
    #down to up
    if m[x - 1][y - 1] == 'S' and m[x + 1][y + 1] == 'M' and m[x + 1][y - 1] == 'M' and m[x - 1][y + 1] == 'S':
        return True

    return False

def count_xmas_occurences_cross():
    m = extract_from_file()
    total_occurences = 0
    for i in range(1, 139):
        for j in range(1, 139):
            if m[i][j] == 'A':
                if is_valid_cross(i, j, m):
                    total_occurences +=1
    
    return total_occurences

if __name__ == "__main__":
    print(count_xmas_occurences())
    print(count_xmas_occurences_cross())