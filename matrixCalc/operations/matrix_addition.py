from operations.elementary_operations import ElementaryOperations as ElementarOP
from matrix import Matrix;

class MatrixAddition:
    
    def __init__(self, matrix1, matrix2):
        self.matrix_sum = Matrix(matrix1.m, matrix1.n)
        self.mx1 = matrix1
        self.mx2 = matrix2

    def calculate_sum(self, substract = False):
        

        if not ElementarOP.check_if_matrix_dims_are_same(self.mx1, self.mx2):
            print("Zadané matice nejsou stejných roměrů!")
            return

        for j in range(self.matrix_sum.n):
            for i in range(self.matrix_sum.m):
                self.matrix_sum.Data[i][j] = self.mx1.Data[i][j] + (self.mx2.Data[i][j] * (-1 if substract else 1))

        return self.matrix_sum