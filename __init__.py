instructions_list = {
    "LOAD":  "00000000 ",
    "ADD":   "00000001 ",
    "SUB":   "00000010 ",
    "JUMP":  "00000100 ",
    "REL":   "00001000 ",
    "COMP":  "00010000 ",
    "IZ":    "00100000 ",
    "NZ":    "01000000 ",
    "POP":   "10000000 ",
    "STORE": "10000001 ",
    "VAR":   "10000010 ",
    "LOG":   "10000100 ",
    "RA1":   "10001000 ",
    "RA2":   "10010000 ",
    "RB1":   "10100000 ",
    "RB2":   "11000000 ",
    "RC1":   "11000001 ",
    "RC2":   "11000010 ",
    "ONE":   "11000100 ",
    "TWO":   "11001000 ",
    "THREE": "11010000 ",
    "FOUR":  "11100000 ",
    "FIVE":  "11100001 ",
    "SIX":   "11100010 ",
    "SEVEN": "11100100 ",
    "EIGHT": "11101000 ",
    "NINE":  "11110000 ",
    "ZERO":  "11110001 "
}

def assemble_instructions(line):
    words = line.split()
    binary_instruction = ""
        
    for word in words:
        if word.endswith(","):
            word = word[:-1]
        if word in instructions_list:
            binary_instruction += instructions_list[word]
        else:
            try:
                binary_instruction += format(int(word), '08b')
            except ValueError:
                raise ValueError(f"error on assemble, unknown word: {word}")
            
    return binary_instruction
        
def assemble_code(file_path):
    binary_code = []
    
    with open(file_path, "r") as file:
        for line in file:
            bin_instruction = assemble_instructions(line)
            binary_code.append(bin_instruction)
                
    return binary_code
    
def main():
    print("#############")
    print("#           #")
    print("# <welcome> #")
    print("#           #")
    print("#############")
    
    cmd = input("insert your command: ")
    
    binary_code = assemble_code(cmd)
        
    for i, binary_instruction in enumerate(binary_code):
        print(f"instruction {i + 1}: {binary_instruction}")
    
if __name__ == "__main__":
    main()