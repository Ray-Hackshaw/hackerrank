def count_substring(string, sub_string):
    position = string.find(sub_string)
    length = len(sub_string)
    count = 1
    for i in range(0, len(string)):
        if position != -1:
            new_string = string[position + 1:position + 1 + length]
            if new_string == sub_string:
                count += 1
            position += 1
        else:
            count = 0
    return count

if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()
    
    count = count_substring(string, sub_string)
    print(count)

# stdin = ABCDCDC
#         CDC

# https://www.hackerrank.com/challenges/find-a-string/problem