# https://www.hackerrank.com/challenges/python-lists/problem

if __name__ == '__main__':
    N = int(input())
    
    list = []
    for _ in range(N):
        c = input().split()
        command = c[0]
        
        if command == "insert":
            list.insert(int(c[1]), int(c[2]))
        elif command == "remove":
            list.remove(int(c[1]))
        elif command == "append":
            list.append(int(c[1]))
        elif command == "sort":
            list.sort()
        elif command == "pop":
            list.pop()
        elif command == "reverse":
            list.reverse()
        else:
            print(list)
