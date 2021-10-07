# https://www.hackerrank.com/challenges/iterables-and-iterators/problem

# Enter your code here. Read input from STDIN. Print output to STDOUT
from itertools import combinations

N = int(input())
elements = input().split()
K = int(input())

comb = list(combinations(elements, K))
total_len = len(comb)

# index = elements[K-1]
count = 0
for each_item in comb:
    if "a" in each_item:
        count += 1

print(count/total_len)
