slopes = [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]


def solve(data):
    v = 0
    trees = 0
    for n, d in enumerate(data):
        if n > 0:
            v += 3
            if d[v%len(d)] == '#':      # modulo to keep v within string length when checking for trees
                trees += 1
    return trees

def solve2(data):
    totaltrees = 1
    for s in slopes:
        v = 0
        trees = 0
        for n, d in enumerate(data):
            if n > 0 and n%s[1]==0:     # skip every s[1]th row (slope down value)
                v += s[0]               # s[0] slope right value
                if d[v%len(d)] == '#':
                    trees += 1
        totaltrees = totaltrees * trees
    return totaltrees


def getdata(filename):
    with open(filename) as f:
        return [l.strip() for l in f.readlines()]
        
if __name__ == '__main__':
    tobmap = (getdata('data_d3.txt'))
    print(solve(tobmap))
    print(solve2(tobmap))