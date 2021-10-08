# https://www.hackerrank.com/challenges/py-collections-namedtuple/problem

# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import namedtuple

total_students = int(input())
columns = input().split()

# Student = namedtuple("Student", "ID MARKS NAME CLASS")
# a = Student(ID=1, MARKS=97, NAME="Raymond", CLASS=7)
# print(a)
# print(a.NAME)

total_mark = 0

for _ in range(total_students):
    students = namedtuple("student", columns)
    col_a, col_b, col_c, col_d = input().split()
    each_student = students(col_a, col_b, col_c, col_d)
    total_mark += int(each_student.MARKS)

print(total_mark / total_students)
