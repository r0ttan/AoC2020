def solve2(data):
    for n,d in enumerate(data):
        for m, e in enumerate(data):
            for o, f in enumerate(data):
                if m != n:
                    if m!= o:
                        if( d + e + f) == 2020:
                            return d * e * f

def solve1(data):
    for n,d in enumerate(data):
        for m, e in enumerate(data):
                if m != n:
                    if( d + e) == 2020:
                            return d * e



def getdata(filename):
    with open(filename) as f:
        indata = [int(i.strip()) for i in f.readlines()]
        #print(indata)
    return indata

if __name__ == '__main__':
    dat = getdata('data_d1.txt')
    print(solve2(dat))
    