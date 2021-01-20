from input_reader import InputReader
from matrix import Matrix
from operations import *
from matrix_console_printer import *
from elementary_operations import *
from helpers import Helpers

class OperationExecutionHandler:
    """Class that handles execution of a given operation. """

    def __init__(self, mx_operation_method, load_data_method):

        self.__read_mx_data = load_data_method; # Pointer na metodu loadu dat
        self.input_reader = InputReader(load_data_method)
        self.__operation = mx_operation_method; # Pointer na metodu zprostředkující danou operaci 
        self.current_operation = None # Reference objektu momentální operace z modulu operations

        # Funkce sloužící ke kontrole rozměrů matice při zadávání hodnot uživatelem
        self.dims_check = lambda x: True 


    def execute(self):
        self.__operation(self);


    def load_data_from_file(self):

        self.input_reader.load_matrix_data_from_file()
        pass

    def load_data_from_console(self):
        print("Zadejte rozměry matice v podobě: mxn \n(tedy např. 3x3):")
        dims = self.input_reader.read_matrix_dimensions(self.dims_check)
        mx = Matrix(dims[1], dims[0])

        print("\nZadejte hodnoty matice po řádcích oddělné mezerou:")
        self.input_reader.read_matrix_user_input(mx)
        return mx            

    def mx_add(self):

        print("\nOperace sčítání:")

        mx1 = self.__read_mx_data(self)

        self.dims_check = lambda sec_mx_dims: Helpers.invalid_dims_addition(sec_mx_dims, mx1)

        mx2 = self.__read_mx_data(self)
        

        MatrixConsolePrinter.print_default(mx1)
        print("(+)")
        MatrixConsolePrinter.print_default(mx2)

        print("-" * (mx2.m * 2 + 1))
        self.current_operation = MatrixSum(mx1, mx2)
        mx_res = self.current_operation.sum()
        MatrixConsolePrinter.print_default(mx_res)

    def mx_sub(self):

        print("\nOperace očítání:")

        print("\nZadejte 1. matici:")
        print("¯ ¯ ¯ ¯ ¯ ¯ ¯ ¯ ¯")
        mx1 = self.__read_mx_data(self)

        print("\nZadejte 2. matici:")
        print("¯ ¯ ¯ ¯ ¯ ¯ ¯ ¯ ¯")

        mx2 = self.__read_mx_data(self)
        
        MatrixConsolePrinter.print_default(mx1)
        print("(-)")
        MatrixConsolePrinter.print_default(mx2)

        print("-" * (mx2.m * 2 + 1))
        self.current_operation = MatrixSum(mx1, mx2)
        mx_res = self.current_operation.sum(substract = True)
        MatrixConsolePrinter.print_default(mx_res)


    def mx_scal(self):

        print("\nOperace násobení skalárem:")

        print("\nZadejte matici:")
        print("¯ ¯ ¯ ¯ ¯ ¯ ¯ ¯")

        mx = self.__read_mx_data(self)


        print("Zadejte skalár:")
        scalar = self.input_reader.read_scalar()

        print(scalar)
        print("(*)")
        MatrixConsolePrinter.print_default(mx)


        print("-" * (mx.m * 2 + 1))
        self.current_operation = MatrixScalarMultiplication(mx, scalar)
        mx_res = self.current_operation.multiply()
        MatrixConsolePrinter.print_default(mx_res)



    def mx_multi(self):

        print("\nOperace násobení matic:")

        print("\nZadejte 1. matici:")
        print("¯ ¯ ¯ ¯ ¯ ¯ ¯ ¯ ¯")
        mx1 = self.__read_mx_data(self)

        self.dims_check = lambda sec_mx_dims: Helpers.invalid_dims_multiplication(sec_mx_dims, mx1)

        print("\nZadejte 2. matici:")
        print("¯ ¯ ¯ ¯ ¯ ¯ ¯ ¯ ¯")

        mx2 = self.__read_mx_data(self)


        MatrixConsolePrinter.print_default(mx1)
        print("(*)")
        MatrixConsolePrinter.print_default(mx2)

        print("-" * (mx2.m * 2 + 1))
        self.current_operation = MatrixMultiplication(mx1, mx2)
        mx_res = self.current_operation.multiply()
        MatrixConsolePrinter.print_default(mx_res)


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

    def mx_pow(self):
        pass
