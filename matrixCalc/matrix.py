class Matrix(object):
    """Base Matrix object."""
    def __init__(self, rows, columns, data = [], name = ""):
        self.m, self.n = rows, columns
        self.Data = data if data != [] else [[0.0]*columns for _ in range(rows)] # První hodnota vybírá řádek (až m-1) druhá hodnota vybírá sloupec (až n-1)
        self.name = name
