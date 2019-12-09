from enum import Enum


class Operation(Enum):
    """
    Operations class defines operation constants

    sub-class is an Enum class
    """

    DELETED = 1
    INSERTED = 2
    SUBSTITUTED = 3

    # def __str__(self):
    #     return str(self.name.lower())


def distances(a, b):
    """
    Calculate edit distance from a to b

    parameters:
    a - string a
    b - string b

    returns edit distance matrix
    """

    # define the height and width of the matrix
    height = len(a) + 1
    width = len(b) + 1

    # create empty matrix of size width x height
    matrix = [[(0, 0) for i in range(width)] for _ in range(height)]

    # edit first element in the matrix
    matrix[0][0] = (0, None)

    # edit first column in matrix with insertion operations
    for row in range(1, height):
        matrix[row][0] = (row, Operation.DELETED)

    # edit first row in matrix with deletion operations
    for column in range(1, width):
        matrix[0][column] = (column, Operation.INSERTED)

    # edit remaining elements of the matrix
    for row in range(1, height):
        for column in range(1, width):
            # calculate deletion cost and insertion cost
            cost_deletion = matrix[row - 1][column][0] + 1
            cost_insertion = matrix[row][column - 1][0] + 1

            # calculate substitution cost, 0 if characters same else +1
            if a[row - 1] == b[column - 1]:
                cost_substitution = matrix[row - 1][column - 1][0]
            else:
                cost_substitution = matrix[row - 1][column - 1][0] + 1

            # find lowest cost and edit this into matrix
            if cost_deletion < cost_insertion and cost_deletion < cost_substitution:
                matrix[row][column] = (cost_deletion, Operation.DELETED)
            elif cost_insertion < cost_deletion and cost_insertion < cost_substitution:
                matrix[row][column] = (cost_insertion, Operation.INSERTED)
            else:
                matrix[row][column] = (cost_substitution, Operation.SUBSTITUTED)

    return matrix