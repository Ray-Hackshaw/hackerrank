if __name__ == '__main__':
    marks = []
    both = []
    for _ in range(int(input())):
        name = input()
        score = float(input())
        marks += [score]
        both += [[name, score]]
    second_lowest = sorted(list(dict.fromkeys(marks)))[1]
    for x, y in sorted(both):
        if second_lowest == y:
            print(x)

# stdin = 5
#         Harry
#         37.21
#         Berry
#         37.21
#         Tina
#         37.2
#         Akriti
#         41
#         Harsh
#         39

# https://www.hackerrank.com/challenges/nested-list/problem