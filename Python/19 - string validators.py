if __name__ == '__main__':
    s = input()
    results = [any(char.isalnum() for char in s), any(char.isalpha() for char in s), any    (char.isdigit() for char in s),
           any(char.islower() for char in s), any(char.isupper() for char in s)]
    for x in results:
        print(x)

# stdin = qA2

# https://www.hackerrank.com/challenges/string-validators/problem