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
        "LOG":   "10000100",
        "RA1":   "10001000",
        "RA2":   "10010000",
        "RB1":   "10100000",
        "RB2":   "11000000",
        "RC1":   "11000001",
        "RC2":   "11000010"
    }
    
    def assemble_instructions(line):
        opcode = line.split()[0]
        if opcode in instructions_list:
            return instructions_list[opcode]
        else:
            raise ValueError(f"error on assemble, unknown command: {opcode}")
    
    def assemble_code():
        code = [
            "LOAD  RA1, 8",
            "LOAD  RA2, 4",
            "ADD   RA1, RA2",
            "STORE RA1",
            "LOG   RA1"
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
            
    if __name__ == "__main__":
        main()