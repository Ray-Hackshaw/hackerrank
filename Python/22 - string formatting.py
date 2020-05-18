def print_formatted(number):
    w = len(bin(number)[2:])
    for x in range(1, number + 1):
        i = str(int(x)).rjust(w, ' ')
        o = oct(int(x))[2:].rjust(w, ' ')
        h = hex(int(x))[2:].upper().rjust(w, ' ')
        b = bin(int(x))[2:].rjust(w, ' ')
        print(i, o, h, b)

if __name__ == '__main__':
    n = int(input())
    print_formatted(n)

# stdin = 17

# https://www.hackerrank.com/challenges/python-string-formatting/problem