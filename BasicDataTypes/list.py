# https://www.hackerrank.com/challenges/python-lists/problem

if __name__ == '__main__':
    N = int(input())

    l = []
    for _ in range(N):
        c = input().split()
        # print(c) # Outputs Lists

        command = c[0]
        # a = int(c[1])
        # b = int(c[2])

        if command in ['insert']:
            if command == 'insert':
                l.insert(int(c[1]),int(c[2]))
        elif command in ['remove', 'append']:
            if command == 'remove':
                l.remove(int(c[1]))
            elif command == 'append':
                l.append(int(c[1]))
        elif command in ['sort','pop','reverse']:
            if command == 'sort':
                l.sort()
            elif command == 'pop':
                l.pop()
            elif command == 'reverse':
                l.reverse()
        else:
            print(l)
