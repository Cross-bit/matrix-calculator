from matrix import *

class MatrixMultiplication:

    def __init__(self, mx1, mx2):
        self.mx1 = mx1
        self.mx2 = mx2
        self.mx_res = Matrix(mx1.m, mx2.n)

    def multiply(self):
        if not self.__check_matrix_dimensions(self.mx1, self.mx2):
            print("Rozměry matic se neshodují")
            return

        for i in range(self.mx1.m):
            for j in range(self.mx2.n):
                for k in range(self.mx1.n):
                    self.mx_res.Data[i][j] += self.mx1.Data[i][k] * self.mx2.Data[k][j]

        return self.mx_res

    def __check_matrix_dimensions(self, mx1, mx2):
        return False if(mx1.n != mx2.m) else True
            
