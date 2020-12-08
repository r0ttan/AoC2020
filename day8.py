from collections import Counter

def solve(data):
    accumulator = 0
    pos = 0
    instr = []
    while pos not in instr and pos < len(data):     #positions are stored in instr, check if we've been here before
        ins, val = data[pos].split()                # split input row to list ['instruction', 'value']
        instr.append(pos)
        if ins == 'nop':
            pos += 1
        elif ins == 'acc':
            accumulator += int(val)
            pos += 1
        elif ins == 'jmp':
            pos += int(val)    
    return accumulator                              # when (before) position is revisited


def solve2(alterinstr, data):
    iteration = 0                                   # to keep track of which instruktion should be changed
    countinstr = Counter(list())                    # -||-
    while iteration < len(data):
        accumulator = 0
        pos = 0                                     # start program from beginning for each iteration
        instr = []
        countinstr.clear()
        while pos not in instr and pos < len(data): # position not revisited and not out of last line of program
            ins, val = data[pos].split()
            instr.append(pos)
            # Not very beautiful way of checking instruction and possibly change of
            if ins == 'nop':
                if countinstr[ins] == iteration and val != 0 and alterinstr == ins:     #trying nop->jmp for every nop with value above 0
                    #treat nop number [iteration] as jmp but count as nop
                    pos += int(val)
                    countinstr.update(['nop'])
                else:
                    countinstr.update(['nop'])
                    pos += 1
            elif ins == 'acc':
                countinstr.update(['acc'])
                accumulator += int(val)
                pos += 1
            elif ins == 'jmp':
                if countinstr[ins] == iteration and alterinstr == ins:
                    #treat as nop, count as jmp
                    pos += 1
                    countinstr.update(['jmp'])
                else:
                    countinstr.update(['jmp'])
                    pos += int(val)
        else:
            if pos == len(data):                    # Alright, we found the exit!
                return accumulator
            else:
                iteration += 1                      # No exit, let's try next instruction
                pos = 0



def getdata(filename):
    with open(filename) as f:
        return f.readlines()       #rows in file to list items
    
        
if __name__ == '__main__':
    data = (getdata('data_d8.txt'))
    test = (getdata('test_d8.txt'))
    #pt1
    #print(solve(data))
    #print(solve(test))
    
    #pt2
    nopsolve = solve2('nop', data)
    if nopsolve:
        print(f'Changed NOP to JMP: {nopsolve}')
    else:
        jmpsolve = solve2('jmp', data)
        print(f'Changed JMP to NOP: {jmpsolve}')
