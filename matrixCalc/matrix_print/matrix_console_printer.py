from matrix import *
from fractions import Fraction
import math
from matrix_print.matrix_print_object import MatrixPrintObject
from matrix_print.column_padding import ColumnPadding


class MatrixConsolePrinter:

    @staticmethod
    def print_default(matrix, get = False, frac = False, round_to = 2):

        matrix_print_object = MatrixPrintObject(matrix, frac, round_to)
        column_padding = ColumnPadding(matrix_print_object)
        padding_for_column = column_padding.get_padding_for_columns()
        
        res = '|'
        res += ' |\n|'.join([''.join(
            [('{:>'+str(padding_for_column[cell_index]+1)+'}').format(row[cell_index])
            for cell_index in range(matrix.n)])
            for row in matrix_print_object.data])
        res += ' |'
        
        print(res)


    @staticmethod
    def print_simple(matrix, get = False, with_zero_rows = False, formated = True):

        res = '\n'.join([''.join(
            [('{:>'+str(padding_for_column[cell_index]+1)+'}').format(row[cell_index])
            for cell_index in range(matrix.n)])
            for row in matrix_print_object.data])

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

