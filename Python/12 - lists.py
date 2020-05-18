if __name__ == '__main__':
    N = int(input())
    int_list = []
    for _ in range(0, N):
        test = input()
        command = test.split()[0]
        if command == "insert":
            index = int(test.split()[1])
            value = int(test.split()[2])
            int_list.insert(index, value)
        if command == "remove":
            remo_val = int(test.split()[1])
            int_list.remove(remo_val)
        if command == "append":
            append_val = int(test.split()[1])
            int_list.append(append_val)
        if command == "sort":
            int_list.sort()
        if command == "reverse":
            int_list.reverse()
        if command == "pop":
            int_list.pop()
        if command == "print":
            print(int_list)


# stdin = 12
#         insert 0 5
#         insert 1 10
#         insert 0 6
#         print
#         remove 6
#         append 9
#         append 1
#         sort
#         print
#         pop
#         reverse
#         print

# https://www.hackerrank.com/challenges/python-lists/problem