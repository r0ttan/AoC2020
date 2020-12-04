import json, re

def getdata(filename):
    passdata = []
    dic = {}
    with open(filename) as f:
        for l in f.readlines():
            if len(l.strip()) == 0:         #string.strip() = None / False on empty line - reached end of passport
                passdata.append(dic.copy())  #dic.copy to cut reference to dictionary appended in list
                dic.clear()
            else:
                for k in l.split():
                    key, val = k.split(':')
                    dic[key] = val
        passdata.append(dic.copy())         # catch last passport (not ending with an empty line)
    return passdata

def solve(fields, data):
    passcount = 0
    for p in data:
        if all(k in p for k in fields):  
            passcount += 1
    return passcount

def solve2(fields, data):
    passcount = 0
    for p in data:
        if all(k in p for k in fields):     # check if all keys in field are present in passport
            for key in p.keys():
                if key != 'cid':            # must check this to avoid krasch when compairing with fields key
                    if not re.search(fields[key], p[key]):      #if one key is invalid...
                        break                                   # ...passport is invalid. Skip to next passport
            else:                          # all tests passed
                passcount += 1      
    return passcount


if __name__ == '__main__':
    passbatch = (getdata('data_d4.txt'))
    val_fld = ['iyr', 'hgt', 'byr', 'pid', 'eyr', 'hcl', 'ecl']
    val_rules = {'iyr':'201[0-9]|2020', 'hgt':'1[5-8][0-9]cm|19[0-3]cm|[59in|[5-6][0-9]in|7[0-6]in', 'byr':'19[2-9][0-9]|2020', 'pid':'[0-9]{9}', 'eyr':'202[0-9]|2030', 'hcl':'#[0-9a-f]{6}', 'ecl':'amb|blu|brn|gry|grn|hzl|oth'}
    print(solve(val_fld, passbatch))
    print(solve2(val_rules, passbatch))
