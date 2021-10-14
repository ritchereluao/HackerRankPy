# https://www.hackerrank.com/challenges/any-or-all/problem

# Enter your code here. Read input from STDIN. Print output to STDOUT

n = int(input())
nums = list(map(int, input().split()))

palindrom_ints = [0,1,2,3,4,5,6,7,8,9,11,22,33,44,55,66,77,88,99,
 101,111,121,131,141,151,161,171,181,191,202,212,
 222,232,242,252,262,272,282,292,303,313,323,333,
 343,353,363,373,383,393,404,414,424,434,444,454,
 464,474,484,494,505,515]

first_condition = all([int(each_num)>0 for each_num in nums])
second_condition = any([each_num for each_num in nums if each_num in palindrom_ints])

print(first_condition and second_condition)
