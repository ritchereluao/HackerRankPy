# https://www.hackerrank.com/challenges/find-angle/problem

# Enter your code here. Read input from STDIN. Print output to STDOUT
from math import atan, degrees

side_ab = int(input())
side_bc = int(input())

calc = atan(1.0 * side_ab / side_bc)
stdout = round(degrees(calc))
degree_sign = u"\N{DEGREE SIGN}"

print(f"{stdout}{degree_sign}")
