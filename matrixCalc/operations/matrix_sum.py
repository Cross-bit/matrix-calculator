from elementary_operations import *

class MatrixSum:
    
    def __init__(self, mx1, mx2):
        self.mx1 = mx1
        self.mx2 = mx1
        self.product = Matrix(mx1.n, mx2.m)

    def sum(self):
        if not (check_if_matrix_dims_are_same(self.mx1, self.mx2)):
            print("Zadané matice nejsou stejných roměrů!")
            return

        for i in range(self.mx1.m):
            for j in range(self.mx2.n):
                self.product = self.mx1[i][j] + self.mx2[i][j]

        return self.product
