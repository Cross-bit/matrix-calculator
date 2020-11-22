from random import Random


class Matrix(object):
    """Matice"""

    def __init__(self, columns, rows, data = [], name = ""):
        self.m, self.n = columns, rows
        self.Data = [[0]*rows for _ in range(columns)] # První hodnota vybírá řádek (až m) druhá hodnota vybírá sloupec (až n)
        self.name = name
        self.rank = 0


            
    



