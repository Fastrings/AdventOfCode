def extract_from_file():
    with open("Day 17\\input.txt") as file:
        lines = file.readlines()
    
    registerA = int(lines[0][11:].strip())
    registerB = int(lines[1][11:].strip())
    registerC = int(lines[2][11:].strip())
    registers = (registerA, registerB, registerC)
    program = list(map(int, lines[4][8:].strip().split(',')))

    return registers, program

def combo(op: int, registers: tuple[int, int, int]) -> int:
    if 0 <= op <= 3:
        return op
    elif op == 4:
        return registers[0]
    elif op == 5:
        return registers[1]
    elif op == 6:
        return registers[2]
    else:
        raise Exception("We done goofed")

def run_program(registers: tuple[int, int, int], program : list[int]) -> list[int]:
    output = []
    i = 0
    registerA, registerB, registerC = registers
    while i in range(len(program)):
        match program[i:i + 2]:
            case 0, op: # adv
                registerA = registerA >> combo(op, (registerA, registerB, registerC))
            case 1, op: # bxl
                registerB = registerB ^ op
            case 2, op: # bst
                registerB = 7 & combo(op, (registerA, registerB, registerC))
            case 3, op: # jnz
                i = op - 2 if registerA else i
            case 4, op: # bxc
                registerB = registerB ^ registerC
            case 5, op: # out
                output = output + [combo(op, (registerA, registerB, registerC)) & 7]
            case 6, op: # bdv
                registerB = registerA >> combo(op, (registerA, registerB, registerC))
            case 7, op: # cdv
                registerC = registerA >> combo(op, (registerA, registerB, registerC))
        i += 2
    
    return output

def find_num_to_output_copy(a: int, i: int) -> int:
    if run_program((a, 0, 0), program) == program:
        print(a)
        exit()
    if run_program((a, 0, 0), program) == program[-i:] or not i:
        for n in range(8):
            find_num_to_output_copy(a * 8 + n, i + 1)

if __name__ == '__main__':
    registers, program = extract_from_file()
    output = run_program(registers, program)
    output = ','.join(map(str, output))
    print("The program will output the following values: ", output)
    print("The lowest number that will cause the program to output itself is: ", end="")
    find_num_to_output_copy(0, 0)