import re
test = ['1-3 a: abcde','1-3 b: cdbefg','2-9 c: acaaaaaaca']

def solve(data):
    count = 0
    for p in data:
        p = p.split()                           # split on whitespace to separate parts of input
        a = p[0].split('-')                     # extract numbers separated by -
        pol = re.findall(f'{p[1][0]}', p[2])    # create list of all ocurrences
        if int(a[0]) <= len(pol) <= int(a[1]):  # compare numbers with length of resulting list from regexp above
            count += 1
    return count

def solve2(data):
    count = 0
    for p in data:
        p = p.split()
        a = [int(i) for i in p[0].split('-')]
        pwd = p[2]                              # for readability, extract password string and control character in own variables
        char = p[1][0] 
        if a[1] <= len(pwd):
            if pwd[a[0]-1] == char and pwd[a[1]-1] != char:
                count += 1
            elif pwd[a[0]-1] != char and pwd[a[1]-1] == char:
                count += 1
    return count

def getdata(filename):
    with open(filename) as f:
        return [l.strip() for l in f.readlines()]
        
if __name__ == '__main__':
    pwdpolicy = (getdata('data_d2.txt'))
    print(solve(pwdpolicy))
    print(solve2(pwdpolicy))
    #solve2(test)
