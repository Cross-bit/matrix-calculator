from matrix import *
from fractions import Fraction
class MatrixConsolePrinter():

    @staticmethod
    def print_default(matrix, get = False):
        res = []
        f_pi = Fraction()
        for i in range(matrix.m):
            res.append("|")
            for j in range(matrix.n):
                f_pi = Fraction(str(matrix.Data[i][j]))
                val = str(f_pi.limit_denominator(100))
                if(j > 0):
                    res.append(" ")
                res.append(val)
                 
            res.append("|\n") if(i < matrix.m-1) else res.append("|")

        if(get == True):
            return "".join(res)
        else:
            print("".join(res))


    @staticmethod
    def print_simple(matrix, get = False, with_zero_rows = False, formated = True):
        res = []
        for i in range(matrix.m):
            zero_ctr = 0
            row_data = []
            for j in range(matrix.n):
                if(matrix.Data[i][j] == 0):
                    zero_ctr += 1
                
                val = str(matrix.Data[i][j])
                if(j > 0):
                    row_data.append(" ")

                row_data.append(val)

            if(i < matrix.m-1):
                row_data.append("\n")

            # Pokud řádek není plný nul přidej
            if(zero_ctr != matrix.n):
                [res.append(row_element) for row_element in row_data]
        
        if(get == True):
            return "".join(res)
        else:
            print("".join(res))


    def get_longest_elemet(self):
        for j in range(self.n):
            for i in range(self.n):
                max_in_row[i] = max(self.Data[i])

        return max(max_in_row)

    def matrix_to_bracket_string(matrix):
        res = []
        res.append("{")
        for i in range(matrix.m):
            res.append("{")
            for j in range(matrix.n):
                val = str(matrix.Data[i][j])
                res.append(val)
                res.append(",") if(j+1 < matrix.n) else ""
                
            res.append("}")
            res.append(",") if(i+1 < matrix.m) else ""

        res.append("}")
        print("".join(res)) 

