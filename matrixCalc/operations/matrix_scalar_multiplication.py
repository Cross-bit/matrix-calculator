from elementary_operations import *

class MatrixScalarMultiplication:

    def __init__(self, mx, scalar):
        self.mx = mx
        self.scalar = scalar
        self.res_mx = Matrix(mx.m, mx.n)
        self.res_mx.Data = mx.Data

    def multiply(self):

        for i in range(self.mx.m):
            ElementaryOperations.multiply_row_by_scalar(self.res_mx, i, self.scalar)

        return self.res_mx


