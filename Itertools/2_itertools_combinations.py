# https://www.hackerrank.com/challenges/itertools-combinations/problem

# Enter your code here. Read input from STDIN. Print output to STDOUT
from itertools import combinations

stdin = input().split()

s = sorted(stdin[0])
k = int(stdin[1])

for num in range(1, k+1):
    stdout = sorted(list(combinations(s, num)))
    for each_item in stdout:
        print("".join(each_item))
