# https://www.hackerrank.com/challenges/collections-counter/problem

from collections import Counter

num_shoes = int(input())
# shoe_sizes = Counter(map(int, input().split()))
shoe_sizes = list(map(int, input().split()))
num_cust = int(input())

earned = 0
for _ in range(num_cust):
    size_desired = list(map(int,input().split()))
    if size_desired[0] in shoe_sizes:
        earned += size_desired[1]
        shoe_sizes.remove(size_desired[0])
print(earned)
