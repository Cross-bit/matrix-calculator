from matrix_print.matrix_print_object import MatrixPrintObject

class ColumnPadding:

    def __init__(self, matrix_print):
        self.matrix_print_object = matrix_print

    def get_padding_for_columns(self):
        return [ (self.__get_longest_val_in_row(col_index))
                for col_index in range(self.matrix_print_object.mx_n)]

    def __get_longest_val_in_row(self, column_index):
        padding_for_columns = len(self.matrix_print_object.data[0][column_index])
        for row_index in range(1, self.matrix_print_object.mx_m):
            row_value_length = len(self.matrix_print_object.data[row_index][column_index])
            if row_value_length > padding_for_columns:
                padding_for_columns = row_value_length
        return padding_for_columns
    
