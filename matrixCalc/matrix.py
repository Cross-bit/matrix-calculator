import random as random

class Matrix(object):
    """Base Matrix object."""
    def __init__(self, rows, columns, data = [], default_cell_value = None):
        self.m, self.n = rows, columns
        self.data = data if data != [] else [[default_cell_value]*columns for _ in range(rows)] # První hodnota vybírá řádek (až m-1) druhá hodnota vybírá sloupec (až n-1)
    
    def generate_random_matrix_data(smallest_val = 0.0, largest_val = 5.0):
        for i in range(self.m):
            for j in range(self.n):
                self.data[i][j] = random.uniform(smallest_val, largest_val)