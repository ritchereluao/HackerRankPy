# https://www.hackerrank.com/challenges/finding-the-percentage/problem

if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()

    while query_name not in student_marks:
        query_name = input()
    else:
        total_score = sum(student_marks[query_name])
        average = total_score/len(student_marks[query_name])
        print("%0.2f"%average)
