# https://www.hackerrank.com/challenges/itertools-combinations-with-replacement/problem

# Enter your code here. Read input from STDIN. Print output to STDOUT
from itertools import combinations_with_replacement

stdin = input().split()

s = sorted(stdin[0])
k = int(stdin[1])

stdout = list(combinations_with_replacement(s, k))

for each_item in stdout:
    print("".join(each_item))
