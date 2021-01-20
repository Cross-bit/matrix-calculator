from elementary_operations import ElementaryOperations as ElementarOP
from matrix import Matrix;

class MatrixSum:
    
    def __init__(self, mx1, mx2):
        self.mx1 = mx1
        self.mx2 = mx2
        self.product = Matrix(mx1.m, mx1.n)

    def sum(self, substract = False):
        if not (ElementarOP.check_if_matrix_dims_are_same(self.mx1, self.mx2)):
            print("Zadané matice nejsou stejných roměrů!")
            return

        print(self.product.m)
        for j in range(self.product.n):
            for i in range(self.product.m):
                self.product.Data[i][j] = self.mx1.Data[i][j] + (self.mx2.Data[i][j] * (-1 if substract else 1))

        return self.product