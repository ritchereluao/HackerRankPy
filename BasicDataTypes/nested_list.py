# https://www.hackerrank.com/challenges/nested-list/problem

if __name__ == '__main__':
    students = []
    for _ in range(int(input())):
        name = input()
        score = float(input())
        students.append([name, score])

    scores = []
    for a,b in students:
        if b not in scores:
            scores.append(b)
    scores = sorted(scores)
    second_lowest = scores[1]

    studs = []
    for a,b in students:
        if b == second_lowest:
            studs.append(a)
    studs = sorted(studs)
    for s in studs:
        print(s)
