# https://www.hackerrank.com/challenges/polar-coordinates/problem

# Enter your code here. Read input from STDIN. Print output to STDOUT
from cmath import sqrt, phase
complex_num = complex(input())

r = sqrt(pow(complex_num.real, 2) + pow(complex_num.imag, 2)).real
y = phase(complex(complex_num.real, complex_num.imag))

print(r)
print(y)
