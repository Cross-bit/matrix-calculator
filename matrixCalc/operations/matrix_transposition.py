from matrix import Matrix

class MatrixTransposition:

    def __init__(self, matrix):
        self.mx = matrix
        self.mx_transposed = Matrix(matrix.n, matrix.m)

    def transpose(self):
        for j in range(self.mx.n):
            for i in range(self.mx.m):
                self.mx_transposed.data[j][i] = self.mx.data[i][j]
        return self.mx_transposed