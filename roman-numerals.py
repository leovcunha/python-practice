# Convert a list of decimals to roman numerals

import sys

n = int(input().strip())
arr = [list(input()) for _ in range(n)]

d5 = ["V", "L", "D", ""]
d1 = ["I","X", "C" ,"M"]

for i in range(n):
    for j in range(len(arr[i])-1,-1,-1): #pick digits from ascending place value (ex: 152 = 2 -> 5 -> 1)
        digit = int(arr[i][j])
        p = len(arr[i])-1-j #place value: 0=units, 1=tens, 2=hundreds, 3=thousands
        if digit == 9:
            r = d1[p]+d1[p+1]
        elif digit > 4 and digit < 9:
            r = d5[p] + (digit-5)*d1[p]
        elif digit == 4:
            r = d1[p]+d5[p] 
        else:
            r = d1[p]*digit
        arr[i][j] = r 
    arr[i] = ''.join(arr[i])
    print(arr[i])
