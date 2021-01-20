from input_reader import InputReader
from matrix import Matrix
from operations import *
from matrix_console_printer import *


class OperationExecutionHandler:
    """Class that handles execution of a given operation. """

    def __init__(self, mx_operation_method, load_data_method):

        self.__read_mx_data = load_data_method; # Pointer na metodu loadu dat
        self.input_reader = InputReader(load_data_method)
        self.__operation = mx_operation_method; # Pointer na metodu zprostředkující danou operaci 
        self.current_operation = None # Reference objektu momentální operace z modulu operations

    def execute(self):
        print(self.__operation)
        self.__operation(self);


    def load_data_from_file(self):

        self.input_reader.load_matrix_data_from_file()
        pass

    def load_data_from_console(self):
        print("Zadejte rozměry matice v podobě: mxn \n(tedy např. 3x3)")
        dims = self.input_reader.read_matrix_dimensions()
        mx = Matrix(dims[1], dims[0])
        self.input_reader.read_matrix_user_input(mx)
        return mx            

    def mx_add(self):

        mx1 = self.__read_mx_data(self)
        mx2 = self.__read_mx_data(self)
        
        print("Operace sčítání:")

        mx1_str = MatrixConsolePrinter.print_simple(mx1, get=True)
        mx2_str = MatrixConsolePrinter.print_simple(mx2, get=True)

        self.current_operation = MatrixSum(mx1, mx2)
        mx_res = self.current_operation.sum()
        mx_res_str = MatrixConsolePrinter.print_simple(mx_res, get=True)

        print(mx1_str, " + ", mx2_str, " = ", mx_res_str, sep = "")

    def mx_sub():
        pass

    def mx_pow():
        pass

    def mx_scal():
        pass

    def mx_multi():
        pass

    def mx_ref():
        pass

    def mx_rref():
        pass

    def mx_trans():
        pass

    def mx_inverse():
        pass

    def mx_rank():
        pass

    def mx_det():
        pass
