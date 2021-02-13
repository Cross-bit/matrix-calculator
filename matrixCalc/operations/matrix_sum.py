from elementary_operations import ElementaryOperations as ElementarOP
from matrix import Matrix;

class MatrixSum:
    
    def __init__(self, matrix1, matrix2):
        self.mx1 = matrix1
        self.mx2 = matrix2
        self.product = Matrix(matrix1.m, matrix1.n)

    def sum(self, substract = False):
        if not (ElementarOP.check_if_matrix_dims_are_same(self.mx1, self.mx2)):
            print("Zadané matice nejsou stejných roměrů!")
            return

        for j in range(self.product.n):
            for i in range(self.product.m):
                self.product.Data[i][j] = self.mx1.Data[i][j] + (self.mx2.Data[i][j] * (-1 if substract else 1))

        return self.product