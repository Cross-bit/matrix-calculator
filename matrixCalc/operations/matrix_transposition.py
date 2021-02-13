from matrix import *
class MatrixTransposition:

    def __init__(self, matrix):
        self.mx = matrix
        self.mx_res = Matrix(matrix.n, matrix.m)

    def transpose(self):

        for j in range(self.mx.n):
            for i in range(self.mx.m):
                self.mx_res.Data[j][i] = self.mx.Data[i][j]
        return self.mx_res