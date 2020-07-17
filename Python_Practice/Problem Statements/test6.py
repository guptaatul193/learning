"""
Sample Input

aaadaa
aa
Sample Output

(0, 1)
(1, 2)
(4, 5)

Output Format

Print the tuple in this format: (start _index, end _index).
If no match is found, print (-1, -1).

Sample Input
"""


import re

if __name__ == '__main__':

    s = input()
    k = input()
    res = re.finditer(r'(?=(%s))' %k,s)
    if not res:
        print((-1,-1))
    else:
        for i in res:
            print((i.start(), i.end(1)-1))
