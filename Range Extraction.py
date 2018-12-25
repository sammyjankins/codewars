# Description:
#
# A format for expressing an ordered list of integers is to use a comma separated list of either
#
#     individual integers
#     or a range of integers denoted by the starting integer separated from the end integer in the range by a dash,
#     '-'. The range includes all integers in the interval including both endpoints. It is not considered a range
#     unless it spans at least 3 numbers. For example ("12, 13, 15-17")
#
# Complete the solution so that it takes a list of integers in increasing order and returns a correctly formatted
# string in the range format.


def solution(args):
    output = []
    first = last = args[0]
    for digit in args[1:] + [""]:
        if digit != last + 1:
            if last == first:
                output.append(str(first))
            elif last == first + 1:
                output.extend([str(first), str(last)])
            else:
                output.append('{}-{}'.format(str(first), str(last)))
            first = digit
        last = digit
    return ",".join(output)


expression_1 = [-6, -3, -2, -1, 0, 1, 3, 4, 5, 7, 8, 9, 10, 11, 14, 15, 17, 18, 19, 20]
expression_2 = [-3, -2, -1, 2, 10, 15, 16, 18, 19, 20, 23]

print(solution(expression_1))
print(solution(expression_2))
