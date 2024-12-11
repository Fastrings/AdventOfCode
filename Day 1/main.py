def extract_from_file():
    left, right = [], []
    with open("Day 1\\input.txt", "r") as file:
        line = file.readline()
        while line:
            line = line.split("   ")
            left.append(int(line[0]))
            right.append(int(line[1]))
            line = file.readline()
    
    return sorted(left), sorted(right)

def total_distance():
    left, right = extract_from_file()
    total_distance = 0
    for i in range(len(left)):
        l, r = left[i], right[i]
        total_distance += abs(l - r)
    
    return total_distance

def similarity_score():
    left, right = extract_from_file()
    l = len(left)
    similarity_score = 0
    for el in left:
        if el in right:
            similarity_score += right.count(el) * el
    
    return similarity_score


if __name__ == "__main__":
    print("Total distance: ", total_distance())
    print("Similarity score: ", similarity_score())