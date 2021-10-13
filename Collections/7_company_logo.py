# https://www.hackerrank.com/challenges/most-commons/problem

from collections import Counter

s = Counter(input()).items()
# print(s)

for letter, num in sorted(s, key=lambda c: (-c[1], c[0]))[:3]:
    print(letter, num)
