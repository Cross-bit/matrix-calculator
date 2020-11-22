from matrix import *
class MatrixTransposition():

    def __delattr__(self, matrix_to_transpose):
        self.mx_to_transpose = matrix_to_transpose
        self.product = Matrix(matrix_to_transpose.m, matrix_to_transpose.n)

    def transpose(self, mx):
        transposed_matrix = Matrix(mx.m, mx.n)

        for j in range(mx.n):
            for i in range(mx.m):
                transposed_matrix.Data[j][i] = mx.Data[i][j]

        return transposed_matrix