from fractions import Fraction
import constants
class MatrixPrintObject:

    def __init__(self, matrix, use_fraction = False, round_to = 2, remove_zeroes = False):
        self.mx_m = matrix.m
        self.mx_n = matrix.n
        self.round_to = round_to
        self.use_frac = use_fraction
        self.remove_zeroes = remove_zeroes
        self.data = self.__convert_data_to_string(matrix.Data)


    def __convert_data_to_string(self, matrix_data):
        formated_data = [0] * self.mx_m;
        for row_index in range(len(matrix_data)):
            temp_row = self.__format_row(matrix_data[row_index])
            if not temp_row: 
                formated_data.pop()
                continue
            formated_data[row_index] = temp_row
        return formated_data

    def __format_row(self, row):
        zero_ctr, row_formated = 0, [0] * self.mx_n;
        for cell_index in range(len(row)):
            if self.remove_zeroes and row[cell_index] < 10.0**((-1)*constants.VALUE_OUTPUT_PRECISION): 
                zero_ctr +=1
            row_formated[cell_index] = str(self.__format_cell_value(row[cell_index])) 
        return False if zero_ctr == self.mx_n else row_formated


    def __format_cell_value(self, cell_value):
        rounded_val = round(cell_value, self.round_to)
        return self.__dec_to_frac(rounded_val) if self.use_frac else rounded_val
    
    def __dec_to_frac(self, data, denominator_limit = 100):
        f_pi = Fraction(str(data))
        return str(f_pi.limit_denominator(denominator_limit))

