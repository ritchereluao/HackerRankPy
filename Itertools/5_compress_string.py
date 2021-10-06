# https://www.hackerrank.com/challenges/compress-the-string/problem

# Enter your code here. Read input from STDIN. Print output to STDOUT
from itertools import groupby

stdin = input()
group_list = [list(g) for k, g in groupby(stdin)]

stdout = []
for each_item in group_list:
    output = []
    output.append(len(each_item))
    output.append(int(each_item[0]))
    stdout.append(tuple(output))

print(*stdout)
