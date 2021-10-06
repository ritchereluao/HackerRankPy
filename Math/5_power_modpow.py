# https://www.hackerrank.com/challenges/python-power-mod-power/problem

a = int(input())
b = int(input())
m = int(input())

stdout_1 = a**b
stdout_2 = (a**b) % m

print(stdout_1)
print(stdout_2)
