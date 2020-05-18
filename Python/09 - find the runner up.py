if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())

arr_list = set(arr)
arr_list.discard(max(set(arr_list)))
print(max(arr_list))

# stdin = 5
#         2 3 6 6 5

# https://www.hackerrank.com/challenges/find-second-maximum-number-in-a-list/problem