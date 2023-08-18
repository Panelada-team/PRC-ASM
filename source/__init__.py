instructions_list = {
    "LOAD":  "00000000",
    "ADD":   "00000001",
    "SUB":   "00000010",
    "JUMP":  "00000100",
    "REL":   "00001000",
    "COMP":  "00010000",
    "IZ":    "00100000",
    "NZ":    "01000000",
    "POP":   "10000000",
    "STORE": "10000001",
    "VAR":   "10000010",
    "LOG":   "10000100"
}

def assemble_instructions(instructions):
    opcode = instructions.split()[0]
    if opcode in instructions_list:
        return instructions_list[opcode]
    else:
        raise ValueError(f"error on assemble, unkown command: {opcode}")

def assemble_code():
    code = [
        "LOAD   RA1, 8",
        "LOAD   RA2, 4",
        "ADD    RA1, RA2",
        "STORE  RA1",
        "LOG    RA1"
    ]
    
    binary_code = []
    
    for line in code:
        bin_instructions = assemble_instructions(line)
        
        binary_code.append(bin_instructions)
        
        return binary_code
        
def main():
    binary_code = assemble_code()
    
    for i, binary_instructions in enumerate(binary_code):
        print(f"instruction {i + 1}: {binary_instructions}")
        
if __name__ == "__init__":
    main()