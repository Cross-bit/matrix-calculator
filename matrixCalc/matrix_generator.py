from random import Random
from matrix import *

class MatrixGenerator:
    
    def __init__(self, number_of_rows, number_of_lines, name = ""):
        self.matrix = Matrix(number_of_rows, number_of_lines)

    def generate_random_values(self, smallest_val = 0, largest_val = 5):
        """
        Volitelné parametery:
        smallest, largest: interval hodnot, kterých můžou hodnoty matice nabývat
        """
        random_generator = Random()
        for i in range(self.m):
            for j in range(self.n):
                self.Data[i][j] = random_generator.randint(smallest_val, largest_val)

    @staticmethod
    def generate_random_matrix(m, n, smallest_val = 0, largest_val = 5):
        """ Generuje random matici 
            Volitelné parametery:
            smallest, largest: interval hodnot, kterých můžou hodnoty matice nabývat
        
        """
        mx = Matrix(m, n)

        random_generator = Random()
        for i in range(mx.m):
            for j in range(mx.n):
                mx.Data[i][j] = random_generator.randint(smallest_val, largest_val)

        return mx

    def get_test_matrix_4x4(self):
            matrix = Matrix(4, 4)

            matrix.Data[0][0] = 1;
            matrix.Data[0][1] = 3;
            matrix.Data[0][2] = 4;
            matrix.Data[0][3] = 0;
            matrix.Data[1][0] = 2;
            matrix.Data[1][1] = 2;
            matrix.Data[1][2] = 2;
            matrix.Data[1][3] = 0;
            matrix.Data[2][0] = 0;
            matrix.Data[2][1] = 2;
            matrix.Data[2][2] = 3;
            matrix.Data[2][3] = 0;
            matrix.Data[3][0] = 2;
            matrix.Data[3][1] = -2;
            matrix.Data[3][2] = -4;
            matrix.Data[3][3] = 0;

            return self.matrix

    def get_test_matrix_3x3_2(self):
        matrix = Matrix(3,3)

        matrix.Data[0][0] = 1;
        matrix.Data[0][1] = 2;
        matrix.Data[0][2] = 3;
        matrix.Data[1][0] = 0;
        matrix.Data[1][1] = 4;
        matrix.Data[1][2] = 5;
        matrix.Data[2][0] = 2;
        matrix.Data[2][1] = 4;
        matrix.Data[2][2] = 6;

        return matrix

