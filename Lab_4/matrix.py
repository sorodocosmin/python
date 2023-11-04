class Matrix:
    """
    A class used to represent a matrix
    All cells in this matrix need to be of the same type (even after applying the apply_function method)
    """

    def __init__(self, rows, cols):
        if type(rows) != int or type(cols) != int:
            print(" ! Invalid matrix size ! (rows and cols must be integers)")
            print("Created 1x1 matrix instead")
            rows = 1
            cols = 1
        elif rows <= 0 or cols <= 0:
            print(" ! Invalid matrix size ! (rows and cols must be > than 0)")
            print("Created 1x1 matrix instead")
            rows = 1
            cols = 1

        self.__rows = rows
        self.__cols = cols
        self.__matrix = [[0 for _ in range(cols)] for __ in range(rows)]
        self.__type_values = None

    def set_cell(self, row, col, value):
        """
        return None if row or col are invalid
        returns True if the cell was set successfully
        return False if it tries to set a cell which has a different type than the other cells
        :param row:
        :param col:
        :param value:
        :return:
        """
        if (type(row) is not int or type(col) is not int or
                row < 0 or row >= self.__rows or col < 0 or col >= self.__cols):
            print(" ! Invalid cell position !")
            return None

        if self.__type_values is None:
            self.__type_values = type(value)
            self.__matrix[row][col] = value
            return True

        elif self.__type_values != type(value):
            print("!All cells in a matrix should be of the same type!")
            return False
        else:
            self.__matrix[row][col] = value
            return True

    def get_cell(self, row, col):
        if (type(row) is not int or type(col) is not int or
                row < 0 or row >= self.__rows or col < 0 or col >= self.__cols):
            print(" ! Invalid cell position !(it will be returned the first cell)")
            return self.__matrix[0][0]

        return self.__matrix[row][col]

    def get_nr_rows(self):
        return self.__rows

    def get_nr_cols(self):
        return self.__cols

    def transpose(self):
        """
        Ex:
        [
        [1, 2, 3],
        [4, 5, 6]
        ]
        ->
        [
        [1, 4],
        [2, 5],
        [3, 6]
        ]
        :return: the transpose of the current matrix
        """
        transpose_matrix = Matrix(self.__cols, self.__rows)
        for i in range(self.__cols):
            for j in range(self.__rows):
                transpose_matrix.set_cell(i, j, self.__matrix[j][i])

        return transpose_matrix

    def multiply(self, other):
        if self.__cols != other.get_nr_rows():
            print(" ! Invalid matrix size for multiplication !")
            return

        matrix_result = Matrix(self.__rows, other.get_nr_cols())
        for i in range(self.__rows):
            for j in range(other.get_nr_cols()):
                sum_of_prod = 0
                for k in range(self.__cols):
                    sum_of_prod += self.__matrix[i][k] * other.get_cell(k, j)

                matrix_result.set_cell(i, j, sum_of_prod)

        return matrix_result

    def apply_function(self, function):
        """
        Apply a function on each cell of the matrix
        :param function: the function that will be applied on each cell
        :return: won't return anything
        """
        new_type = type(function(self.__matrix[0][0]))
        new_matrix = []
        for i in range(self.__rows):
            line = []
            for j in range(self.__cols):
                res = function(self.__matrix[i][j])
                if type(res) != new_type:
                    print(" ! Error at apply_function method !")
                    print(" ! The function should return values of the same type for all values of the matrix !")
                    print(" ! The matrix was not modified !")
                    return
                else:
                    line.append(res)

            new_matrix.append(line)

        self.__type_values = new_type
        self.__matrix = new_matrix

    def __mul__(self, other):
        return self.multiply(other)

    def __eq__(self, other):
        if self.__rows != other.get_nr_rows() or self.__cols != other.get_nr_cols():
            return False

        for i in range(self.__rows):
            for j in range(self.__cols):
                if self.__matrix[i][j] != other.get_cell(i, j):
                    return False

        return True

    def __str__(self):
        # return a string representation of the matrix
        str_matrix = "[\n"

        for row in self.__matrix:
            str_matrix += str(row) + "\n"

        str_matrix += "]"

        return str_matrix

