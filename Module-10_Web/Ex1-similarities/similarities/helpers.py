from enum import Enum


class Operation(Enum):
    """Operations"""

    DELETED = 1
    INSERTED = 2
    SUBSTITUTED = 3

    # def __str__(self):
    #     return str(self.name.lower())


def distances(a, b):
    """Calculate edit distance from a to b"""

    matrix = [[(0,0) for i in range(len(a) + 1)] for _ in range(len(b) + 1)]

    matrix[0][0] = (0, None)

    for row in range(1,len(a) + 1):
        matrix[row][0] = (row, Operation(2))

    for column in range(1,len(b) + 1):
        matrix[0][column] = (column, Operation(1))
        
    for row in range(1, len(a) + 1):
        for column in range(1, len(b) + 1):
            cost_deletion = matrix[row - 1][column][0] + 1
            cost_insertion = matrix[row][column - 1][0] + 1

            if a[row - 1] == b[column - 1]:
                cost_substitution = matrix[row - 1][column - 1][0]
            else:
                cost_substitution = matrix[row - 1][column - 1][0] + 1

            if cost_deletion < cost_insertion and cost_deletion < cost_substitution:
                matrix[row][column] = (cost_deletion, Operation(1))
            elif cost_insertion < cost_deletion and cost_insertion < cost_substitution:
                matrix[row][column] = (cost_insertion, Operation(2))
            else:
                matrix[row][column] = (cost_substitution, Operation(3))

    # for row in matrix:
    #     for element in row:
    #         print(element[0], end=" ")
    #     print()

    return matrix
