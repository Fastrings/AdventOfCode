def extract_from_file():
    with open("Day 9\\input.txt") as file:
        return file.read().strip()

def diskmap_to_blocks(diskmap: str) -> list[str]:
    blocks = []
    id = 0
    for i, item in enumerate(diskmap):
        num = int(item)
        if i % 2 == 0:
            blocks.extend([id] * num)
            id += 1
        else:
            blocks.extend(['.'] * num)
    return blocks

def organize_blocks(blocks: str) -> list[str]:
    split_blocks = list(blocks)
    left = 0
    right = len(split_blocks) - 1
    while True:
        while split_blocks[left] != '.':
            left += 1
        while split_blocks[right] == '.':
            right -= 1
        if left > right:
            break
        
        split_blocks[left], split_blocks[right] = split_blocks[right], split_blocks[left]
    
    return split_blocks

def compute_checksum(blocks: str) -> int:
    return sum(i * int(x) for i, x in enumerate(blocks) if x != '.')

def find_available_space(blocks: list[str], file_position: int, length: int) -> int:
    for i in range(file_position - length):
        l = 0
        j = i
        while blocks[j] == '.':
            j += 1
            l += 1
            if l == length:
                return i
    return -1

def organize_files(blocks: str) -> list[str]:
    split_blocks = list(blocks)
    right = len(split_blocks) - 1
    while True:
        #print(split_blocks)
        file_size = 0
        av_space_len = 0
        id = None
        while right >= 0:
            item = split_blocks[right]
            if item == '.' and file_size == 0:
                right -= 1
            elif item != '.' and (id == None or id == item):
                id = item
                right -= 1
                file_size += 1
            else:
                break
        
        left = 0
        while left <= right:
            item = split_blocks[left]
            if item == '.':
                av_space_len += 1
                if av_space_len == file_size:
                    for temp in range(file_size):
                        l, r = left - av_space_len + temp + 1, right + 1 + temp
                        split_blocks[l], split_blocks[r] = split_blocks[r], split_blocks[l]
                    break
            else:
                av_space_len = 0
            left += 1
        
        if right < 0:
            break
    
    return split_blocks

if __name__ == "__main__":
    dm = extract_from_file()
    blocks = diskmap_to_blocks(dm)

    blocks = organize_blocks(blocks)
    check = compute_checksum(blocks)
    print("Checksum part 1: ", check)

    blocks2 = organize_files(blocks)
    check2 = compute_checksum(blocks2)
    print("Checksum part2: ", check2)