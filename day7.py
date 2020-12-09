import re

result = set()
result2 = []

def solve(col, rules):
    parentcol = ''
    global result
    for d in rules:
        searchstr = f'^(?!\\b{col}\\b).*\\b{col}\\b'
        if (re.search(searchstr, d)):
            parentcol = ' '.join(d.split()[:2])
            result.add(solve(parentcol, rules))
    result.add(col)
    return parentcol



# not proud of this but finally got it to work
def solve2(col, rules):
    global result2
    noofbag = ''
    for d in rules:
        searchstr = f'^\\b{col}\\b.*'
        if (re.search(searchstr, d)):
            childcols = ' '.join(c for c in d.split()[4:]).split(',') #unforgiving ugly unreadable way of parsing data rows
            # d.split()[4:], split -> list of words, slice list from index 4 to end
            # ' '.join(...) list of all words for child (amount and colours) -> string
            # split(',') -> list of strings with amount and colour for each child-bag, sigh

            for chc in childcols:
                bagamount = chc.split()  #string -> list of words
                ccolour = ' '.join(bagamount[1:3])  # second and third item will always be a two word colour
                noofbag = bagamount[0]              # first item in list is amount of bags
                if noofbag.strip() != 'no':         # some bags dont contain any other bags
                    result2.append(noofbag)         
                    for r in range(int(noofbag)):   
                        solve2(ccolour, rules)      # for every bag in every bag and so on
    
    return noofbag




def getdata(filename):
    with open(filename) as f:
        return f.readlines()       #rows in file to list items
        
        
if __name__ == '__main__':
    mybagcol = 'shiny gold'
    rules = (getdata('data_d7.txt'))
    #test = (getdata('test_d7.txt'))
    #pt1
    solve(mybagcol, rules)
    print(len([r for r in result if r != '' and r != mybagcol]))
    #pt2
    solve2(mybagcol, rules)
    print(sum(int(r) for r in result2 if r.isdigit()))
