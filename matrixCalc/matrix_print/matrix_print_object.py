from fractions import Fraction
class MatrixPrintObject:

    def __init__(self, matrix, use_fraction = False, round_to = 2):
        self.mx_m = matrix.m
        self.mx_n = matrix.n
        self.round_to = round_to
        self.use_frac = use_fraction
        self.data = self.__convert_data_to_string(matrix.Data)

    def __convert_data_to_string(self, matrix_data):
        return [[str(self.__format_cell_value(cell)) for cell in row] for row in matrix_data]

    def __format_cell_value(self, cell_value):
        rounded_val = round(cell_value, self.round_to)
        return self.__dec_to_frac(rounded_val) if self.use_frac else rounded_val
    
    def __dec_to_frac(self, data, denominator_limit = 100):
        f_pi = Fraction(str(data))
        return str(f_pi.limit_denominator(denominator_limit))

