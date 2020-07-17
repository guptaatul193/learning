"""
You are given a string S. It consists of alphanumeric characters, spaces and symbols(+,-).
Your task is to find all the substrings of S that contains 2 or more vowels.
Also, these substrings must lie in between 2 consonants and should contain vowels only.

"""
import re

def check(i,inp):
    if i.start() == 0:
        return False
    elif i.end() == len(inp):
        return False
    elif re.match( r'[b-df-hj-np-tv-zB-DF-HJ-NP-TV-Z]' , inp[i.start()-1]) == None:
        return False
    elif re.match( r'[b-df-hj-np-tv-zB-DF-HJ-NP-TV-Z]' , inp[i.end()]) == None:
        return False
    return True



if __name__ == '__main__':
    
    inp = input()

    x = re.finditer(r'[AEIOUaeiou]{2,}', inp )

    out=[]
    for i in x:
        if check(i,inp): out.append(i.group())


    if out==[]:
        print(-1)
    else:
        for i in out:
            print(i)
