if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()
    scores = student_marks.get(query_name)
    avg = (sum(scores)/len(scores))
    print("{0:.2f}".format(avg))

# stdin = 2
#         Harsh 25 26.5 28
#         Anurag 26 28 30
#         Harsh

# https://www.hackerrank.com/challenges/finding-the-percentage/problem