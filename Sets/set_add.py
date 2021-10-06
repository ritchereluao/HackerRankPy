# https://www.hackerrank.com/challenges/py-set-add/problem

# Enter your code here. Read input from STDIN. Print output to STDOUT

n = int(input())
stdout = set("")
for _ in range(n):
    country = input()
    stdout.add(country)
print(len(stdout))
