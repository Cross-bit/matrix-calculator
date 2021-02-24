from matrix import Matrix
from matrix_print.matrix_print_object import MatrixPrintObject
from matrix_print.column_padding import ColumnPadding
import constants

class MatrixConsolePrinter:

    @staticmethod
    def print_default(matrix):

        matrix_print_object = MatrixPrintObject(matrix, constants.FRACTION_OUTPUT, constants.VALUE_OUTPUT_PRECISION)
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
    def print_simple(matrix, get = False):

        matrix_print_object = MatrixPrintObject (matrix, constants.FRACTION_OUTPUT, constants.VALUE_OUTPUT_PRECISION)

        res = ''
        res += '\n'.join([' '.join([cell for cell in row]) for row in matrix_print_object.data])

        return res if get else print(res)

    @staticmethod
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

