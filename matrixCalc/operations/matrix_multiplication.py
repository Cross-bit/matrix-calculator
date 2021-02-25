from matrix import Matrix

class MatrixMultiplication:

    def __init__(self, matrix1, matrix2):
        self.mx1 = matrix1
        self.mx2 = matrix2
        self.mx_res = Matrix(matrix1.m, matrix2.n)

    def calculate_multiplication(self):
        if not self.__check_matrix_dimensions(self.mx1, self.mx2):
            raise Exception("Rozměry matic nejsou platné!")

        for i in range(self.mx1.m):
            for j in range(self.mx2.n):
                cell_value = 0
                for k in range(self.mx1.n):
                   cell_value += self.mx1.data[i][k] * self.mx2.data[k][j]
                self.mx_res.data[i][j] = cell_value

        return self.mx_res

    def __check_matrix_dimensions(self, mx1, mx2):
        return False if(mx1.n != mx2.m) else True
            
