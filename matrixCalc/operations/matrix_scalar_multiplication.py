from elementary_operations import ElementaryOperations
from matrix import Matrix

class MatrixScalarMultiplication:

    def __init__(self, matrix, scalar):
        self.mx = matrix
        self.scalar = scalar
        self.res_mx = Matrix(matrix.m, matrix.n)
        self.res_mx.data = matrix.data

    def calculate_scalar_multiplication(self):

        for i in range(self.mx.m):
            ElementaryOperations.multiply_row_by_scalar(self.res_mx, i, self.scalar)

        return self.res_mx


