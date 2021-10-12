# https://www.hackerrank.com/challenges/word-order/problem

# Enter your code here. Read input from STDIN. Print output to STDOUT

from collections import OrderedDict
n = int(input())
d = OrderedDict()

for _ in range(n):
    each_word = input()
    d.setdefault(each_word, 0)
    d[each_word] += 1

# print(d)
print(len(d))
print(*d.values())
