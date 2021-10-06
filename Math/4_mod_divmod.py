# https://www.hackerrank.com/challenges/python-mod-divmod/problem

# Enter your code here. Read input from STDIN. Print output to STDOUT
first_num = int(input())
second_num = int(input())

num = first_num // second_num
remainder = first_num % second_num
stdout = divmod(first_num, second_num)

print(num)
print(remainder)
print(stdout)
