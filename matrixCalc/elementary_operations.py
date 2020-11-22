from matrix import *
class ElementaryOperations:
    """
    Základní maticové úpravy a operace
    """
    @staticmethod
    def check_if_matrix_dims_are_same(mx1, mx2):
        return True if(mx1.m == mx2.m and mx1.n == mx2.n) else False

    @staticmethod
    def exchange_rows(mx, row1, row2):
        """
        Výměna řádků matice. row1, row2 odpovídají indexům řádků, které mají být prohozeny (počínaje 0).
        V případě poskytnutí špatných rozsahů indexů hodí výjimku.
        """
        
        if(row1 >= mx.m or row2 >= mx.m):
            raise Exception("Indexy sahají mimo rozsah matice!")
            return

        # Projde jednotlivé hodnoty řádků a prohodí je
        for j in range(mx.n):
            mx.Data[row1][j], mx.Data[row2][j] = mx.Data[row2][j], mx.Data[row1][j]

    @staticmethod 
    def multiply_row_by_scalar(mx, row, scalar):
        """
        Projde všechny prvky o indexu row a vynásobí konstantou scalar
        """

        if(row >= mx.m):
            raise Exception("Řádek matice neexistuje!")

        for j in range(mx.n):
            mx.Data[row][j] *= scalar

    @staticmethod 
    def add_two_rows(mx, row1, row2):
        """
        Přičtení řádku row1 k řádku row2.
        """

        if(row1 >= mx.m or row2 >= mx.m):
            raise Exception("Řádek matice neexistuje!")

        for j in range(mx.n):
            mx.Data[row2][j] += mx.Data[row1][j]

    @staticmethod
    def find_first_most_left_value(mx, start_row, start_col):
        """
        Vrací souřadnice jako tuple (row, col), první nalezené hodnoty nejvíce v levo. Hledaná oblast je vymezena parametry:
         - start_row
         - start_col       
        """
        for l in range(start_col, mx.n):
            for r in range(start_row, mx.m):
                if(mx.Data[r][l] != 0):
                    return (r, l)
        return (0, 0)





