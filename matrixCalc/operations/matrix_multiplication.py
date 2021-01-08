from matrix import *

class MatrixMultiplication:

    def __init__(self, mx1, mx2):
        self.mx1 = mx1
        self.mx2 = mx2
        self.product = Matrix(mx1.m, mx2.n)#TODO:

    def multiply_matrices(self, mx1, mx2):
        if not self.check_matrix_dimensions(mx1, mx2):
            print("Rozměry matic se neshodují")
            return

        mx_res = Matrix(mx1.m, mx2.n)

        for i in range(mx1.m):
            for j in range(mx2.n):
                for k in range(mx1.n):
                    mx_res.Data[i][j] += mx1.Data[i][k] * mx2.Data[k][j]

        return mx_res

    def check_matrix_dimensions(self, mx1, mx2):
        return False if(mx1.n != mx2.m) else True
            
