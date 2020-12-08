

def solve(data):
    accumulator = 0
    pos = 0
    instr = []
    while pos not in instr and pos < len(data):
        ins, val = data[pos].split()
        instr.append(pos)
        if ins == 'nop':
            pos += 1
        elif ins == 'acc':
            accumulator += int(val)
            pos += 1
        elif ins == 'jmp':
            pos += int(val)    
    return accumulator

def solve2():
    pass


def getdata(filename):
    with open(filename) as f:
        return f.readlines()       #rows in file to list items
    
        
if __name__ == '__main__':
    data = (getdata('data_d8.txt'))
    test = (getdata('test_d8.txt'))
    print(solve(data))
    #print(solve(test))