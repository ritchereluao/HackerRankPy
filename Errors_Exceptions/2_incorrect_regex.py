# https://www.hackerrank.com/challenges/incorrect-regex/problem

# Enter your code here. Read input from STDIN. Print output to STDOUT
import re

t = int(input())

for _ in range(t):
    try:
        re.compile(input())
    except:
        re.error: print(False)
    else:
        print(True)
