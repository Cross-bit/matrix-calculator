class Matrix(object):
    """Base Matrix object."""

    def __init__(self, rows, columns, data = [], name = ""):
        self.m, self.n = rows, columns
        self.Data = [[0]*columns for _ in range(rows)] # První hodnota vybírá řádek (až m) druhá hodnota vybírá sloupec (až n)
        self.name = name
        self.rank = 0


            
    



