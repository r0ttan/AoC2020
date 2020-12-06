from collections import Counter

def solve(data):
    c = Counter()               
    q = 0                           # total number of yes-questions
    for i in data:                  # for each row
        if len(i.strip()) > 0:      # not empty line
            c.update(i.strip())     # collects all unique qestions and how many answers as dict e.g. {'a':4, 'b':1}
        else:                       # empty line = group end
            for v in c.keys():      
                q += 1              # count number of yes answers
            c.clear()               # empty the counter before counting next group
    for v in c.keys():              # catch last group not ending with empty line
        q += 1
    return q

def solve2(data):
    c = Counter()
    q = 0
    p = 0                           # number of persons in group
    for i in data:
        if len(i.strip()) > 0:
            p += 1                  # every line i group = 1 person
            c.update(i.strip())
        else:
            for v in c.values():    
                if v == p:          # count only questions where no of ppl in group = no of answers
                    q += 1
            c.clear()
            p = 0
    for v in c.values():
        if v == p:
            q += 1
    return q


def getdata(filename):
    with open(filename) as f:
        return f.readlines()       #rows in file to list items
        
        
if __name__ == '__main__':
    dat = (getdata('data_d6.txt'))
    #test = (getdata('test_d6.txt'))
    print(solve(dat))
    print(solve2(dat))
    