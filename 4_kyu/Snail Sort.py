# Snail Sort
# Given an n x n array, return the array elements arranged from outermost elements to the middle element,
# traveling clockwise.
#
# array = [[1,2,3],
#          [4,5,6],
#          [7,8,9]]
# snail(array) #=> [1,2,3,6,9,8,7,4,5]
# For better understanding, please follow the numbers of the next array consecutively:
#
# array = [[1,2,3],
#          [8,9,4],
#          [7,6,5]]
# snail(array) #=> [1,2,3,4,5,6,7,8,9]
#
# NOTE: The idea is not sort the elements from the lowest value to the highest;
# the idea is to traverse the 2-d array in a clockwise snailshell pattern.
#
# NOTE 2: The 0x0 (empty matrix) is represented as [[]]


def matrix_rot(matrix):
    out = []
    if not matrix:
        return
    for i, _ in enumerate(matrix[0]):
        out.append([])
        for row in matrix:
            out[-1].append(row[-1 - i])
    return out


def snail(array):
    out = []
    while array:
        out += array.pop(0)
        array = matrix_rot(array)
    return out


array = [[1, 2, 3],
         [8, 9, 4],
         [7, 6, 5]]
print(snail(array))
