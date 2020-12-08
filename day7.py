import re

result = set()

def solve(col, rules):
    parentcol = ''
    global result
    for n,d in enumerate(rules):
        searchstr = f'^(?!\\b{col}\\b).*\\b{col}\\b'
        if (re.search(searchstr, d)):
            parentcol = ' '.join(d.split()[:2])
            result.add(solve(parentcol, rules))
    result.add(col)
    return parentcol

# unfinished
def solve2(col, rules):
    childcol = ''
    global result
    for n,d in enumerate(rules):
        searchstr = f'^\\b{col}\\b.*'
        #searchstr = f'^(?!\\b{col}\\b).*\\b{col}\\b'
        if (re.search(searchstr, d)):
            childcols = ' '.join(c for c in d.split()[4:]).split(',')
            for chc in childcols:
                ccolour = ' '.join(chc.split()[1:3])
                print(f'Search {col} in "{d}". chc{chc}, ccolour{ccolour}')
                result.add(solve2(chc, rules))
            #result.add(solve(parentcol, rules))
    result.add(col)
    return childcol


def getdata(filename):
    with open(filename) as f:
        return f.readlines()       #rows in file to list items
        
        
if __name__ == '__main__':
    mybagcol = 'shiny gold'
    rules = (getdata('data_d7.txt'))
    test = (getdata('test_d7.txt'))
    solve(mybagcol, rules)
    #solve2(mybagcol, test)
    #print(result)
    realres = [r for r in result if r != '' and r != mybagcol]
    print(len(realres))
   