from collections import defaultdict

def extract_from_file() -> list[int]:
    with open("Day 22\\input.txt") as file:
        return [int(line.strip()) for line in file]

def process_secret_number(secret_number):
    MODULO = 16777216  # Used for pruning
    
    # Step 1
    step1_result = secret_number * 64
    secret_number ^= step1_result  # Mix
    secret_number %= MODULO  # Prune

    # Step 2
    step2_result = secret_number // 32
    secret_number ^= step2_result  # Mix
    secret_number %= MODULO  # Prune

    # Step 3
    step3_result = secret_number * 2048
    secret_number ^= step3_result  # Mix
    secret_number %= MODULO  # Prune

    return secret_number

def process_list_buyers(buyer_secrets: list[int]) -> int:
    total = 0
    for s in buyer_secrets:
        for _ in range(2000):
            s = process_secret_number(s)
        
        total += s
    
    return total

def find_max_number_of_bananas(buyer_secrets: list[int]) -> int:
    total_bananas = defaultdict(int)
    for b in buyer_secrets:
        seen = set()
        price_changes = []
        for i in range(2000):
            next_secret = process_secret_number(b)
            price_changes.append((next_secret % 10) - (b % 10))
            b = next_secret
            if i >= 3:
                sequence = tuple(price_changes)
                if sequence not in seen:
                    total_bananas[sequence] += b % 10
                    seen.add(sequence)
                price_changes.pop(0)
    
    return max(total_bananas.values())

if __name__ == '__main__':
    secrets = extract_from_file()
    print("Sum of all 2000th secret numbers of each buyer: ", process_list_buyers(secrets))
    print("Maximum amount of bananas obtainable: ", find_max_number_of_bananas(secrets))