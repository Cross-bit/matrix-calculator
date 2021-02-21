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