def solve(data):    
    for n, d in enumerate(data):
        cont = False
        if n > 24:
            for e in data[n-25:n]:
                for f in data[n-25:n]:
                    if e + f == d and e != f:
                        cont = True
                        break
                if cont:
                    break
            if not cont:            
                #print(f'{d}\n')
                return d
    return True 

def solve2(failnum, data):
    failn = failnum
    contrange = []
    contsum = 0
    for n, d in enumerate(data):
        contrange.clear()
        failn -= d
        contsum += d
        pos = n   
        contrange.append(d)
        while failn > 0:
            pos += 1
            failn -= data[pos]
            contrange.append(data[pos])
            if failn == 0:
                return min(contrange), max(contrange)
            elif failn < 0:
                failn = failnum
                break

def getdata(filename):
    with open(filename) as f:
        nums = [ int(n.strip()) for n in f.readlines()]
        return nums       #rows in file to list items
    
        
if __name__ == '__main__':
    data = (getdata('data_d9.txt'))
    test = (getdata('test_d9.txt'))
    fn = solve(data)
    print(fn)
    low, high = solve2(fn, data)
    print(f'low {low} + high {high} = {low + high}')
