# https://www.hackerrank.com/challenges/itertools-permutations/problem

# Enter your code here. Read input from STDIN. Print output to STDOUT
from itertools import permutations

stdin = input().split()
s = stdin[0]
i = int(stdin[1])

stdout = sorted(list(permutations(s, i)))

for each_item in stdout:
    print("".join(each_item))
    
