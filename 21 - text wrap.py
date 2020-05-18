import textwrap
import re

def wrap(string, max_width):
    v = '\n'.join(textwrap.wrap(string, max_width))
    return v

if __name__ == '__main__':
    string, max_width = input(), int(input())
    result = wrap(string, max_width)
    print(result)

# stdin = ABCDEFGHIJKLIMNOQRSTUVWXYZ
#         4

# https://www.hackerrank.com/challenges/text-wrap/problem