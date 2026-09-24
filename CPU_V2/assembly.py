ALU = {
    'ADD':'0010', 'SUB':'0011', 'NOR':'0100', 'AND':'0101', 
    'XOR':'0110', 'RSH':'0111','LDI':'1000','ADI':'1001',
    'INC':'1001','DEC':'1001'
    }

WRITE = {
    'R1':'0001', 'R2':'0010', 'R3':'0011', 'R4':'0100', 'R5':'0101', 'R6':'0110', 'R7':'0111', 'R8':'1000',
    'R9':'1001', 'R10':'1010', 'R11':'1011', 'R12':'1100', 'R13':'1101', 'R14':'1110', 'R15':'1111',
}


tokens = []

with open('fichier.txt', 'r') as f:
    for ligne in f:
        tokens = ligne.strip().split()
        instr = tokens[0]

        if instr in ALU:
            opcode = ALU[instr]
            
            if instr == 'LDI':
                write = WRITE[tokens[1]]
                value = bin(int(tokens[2]))[2:].zfill(8)

                code_machine = opcode + ' ' + write  + ' ' + value[0:4] + ' ' + value[4:8] 

            elif instr == 'RSH':
                read = WRITE[tokens[1]]

                code_machine = opcode + ' ' + read + ' ' + '0000' + ' ' + read

            elif instr == 'ADI':
                read = WRITE[tokens[1]]
                value = bin(int(tokens[2]))[2:].zfill(8)

                code_machine = opcode + ' ' + read + ' ' + value[0:4] + ' ' + value[4:8] 

            elif instr == 'INC':
                read = WRITE[tokens[1]]

                code_machine = opcode + ' ' + read + ' ' + '0000' + ' ' + '0001'

            elif instr == 'DEC':
                read = WRITE[tokens[1]]

                code_machine = opcode + ' ' + read + ' ' + '1111' + ' ' + '1111'

            else:
                write = WRITE[tokens[3]]
                read1 = WRITE[tokens[1]]
                read2 = WRITE[tokens[2]]
            
                code_machine = opcode + ' ' + read1 + ' ' + read2 + ' ' + write

            print(code_machine)
