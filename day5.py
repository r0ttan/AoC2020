"""
BFFFBBFRRR: row 70, column 7, seat ID 567.
FFFBBBFRRR: row 14, column 7, seat ID 119.
BBFFBBFRLL: row 102, column 4, seat ID 820.
"""



def solve(data):
    seatlist = []
    for i in data:
        row = [r for r in range(128)]
        col = [c for c in range(8)]    
        for s in i[:7]:
            if s == 'B':
                row = (row[int(len(row)/2):])       # slice list from higher middle to end
            if s == 'F':
                row = (row[:(int(len(row)/2))])     # slice from start to lower middle
        for t in i[7:]:
            if t == 'R':
                col = (col[int(len(col)/2):])
            if t == 'L':
                col = (col[:int(len(col)/2)])
        seatlist.append(row[0]*8+col[0])
    return sorted(seatlist)

def solve2(seatlist):
    for n, s in enumerate(seatlist):
        if s == seatlist[0]+n:
            pass
            #print(s, seatlist[0]+n)
        else:
            return s-1


def getdata(filename):
    with open(filename) as f:
        return f.readlines()       #rows in file to list items
        
        
if __name__ == '__main__':
    dat = (getdata('data_d5.txt'))
    #print(solve(['BFFFBBFRRR', 'FFFBBBFRRR','BBFFBBFRLL']))
    #print(solve(dat))
    print(solve2(solve(dat)))