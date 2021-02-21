from input_output.input_reader import InputReader
from matrix import Matrix
from operations import *
from matrix_print.matrix_console_printer import *
from elementary_operations import *
from helpers import Helpers


class OperationExecution:
    """ Stará se o průběh a exekuci operací kalkulačky."""

    def __init__(self, mx_operation_method, load_data_method):

        self.__read_mx_data = load_data_method;
        self.input_reader = InputReader()
        self.__operation = mx_operation_method; # Pointer na metodu zprostředkující danou operaci 

        self.current_operation = None # Reference objektu momentální operace z modulu operations
        self.operation_result = None

        # Funkce sloužící ke kontrole rozměrů matice při zadávání hodnot uživatelem
        self.dims_check = lambda x: True 


    def execute(self):
        self.__operation(self);

    def __get_matrix_dims(self):
        print("Zadejte rozměry matice celými čísly, ve tvaru: mxn \n(tedy např. 2x2):")
        return self.input_reader.read_matrix_dimensions(self.dims_check)

    def load_data_from_file(self):

        print("Zadejte název cílového souboru ve formátu .txt (stačí bez přípony):")
        data_file_name = input()

        mx_data = self.input_reader.read_matrix_data_from_file(data_file_name);

        if mx_data:
            mx = Matrix(len(mx_data), len(mx_data[0]), mx_data)
            dims = (mx.m, mx.n)

            if(self.dims_check(dims)):
                return mx
            else:
                print("Zkuste prosím jiný soubor:")


        return self.load_data_from_file();

    def load_data_from_console(self):
        dims = self.__get_matrix_dims()
        mx = Matrix(dims[0], dims[1])

        print("\nZadejte hodnoty matice po řádcích oddělné mezerou:")
        self.input_reader.read_matrix_user_input(mx)

        return mx            

    def mx_add(self):

        print("\nOperace sčítání:")

        print("\nZadání 1. matice:")
        print("¯ ¯ ¯ ¯ ¯ ¯ ¯ ¯ ¯")

        mx1 = self.__read_mx_data(self)

        self.dims_check = lambda sec_mx_dims: Helpers.invalid_dims_addition(sec_mx_dims, mx1)

        print("\nZadání 2. matice:")
        print("¯ ¯ ¯ ¯ ¯ ¯ ¯ ¯ ¯")

        mx2 = self.__read_mx_data(self)
        

        MatrixConsolePrinter.print_default(mx1)
        print("(+)")
        MatrixConsolePrinter.print_default(mx2)

        print("-" * (mx2.m * 2 + 1))
        self.current_operation = MatrixAddition(mx1, mx2)
        mx_res = self.current_operation.sum()
        MatrixConsolePrinter.print_default(mx_res)

    def mx_sub(self):

        print("\nOperace očítání:")

        print("\nZadání 1. matice:")
        print("¯ ¯ ¯ ¯ ¯ ¯ ¯ ¯ ¯")
        mx1 = self.__read_mx_data(self)

        self.dims_check = lambda sec_mx_dims: Helpers.invalid_dims_addition(sec_mx_dims, mx1)

        print("\nZadání 2. matice:")
        print("¯ ¯ ¯ ¯ ¯ ¯ ¯ ¯ ¯")

        mx2 = self.__read_mx_data(self)
        
        MatrixConsolePrinter.print_default(mx1)
        print("(-)")
        MatrixConsolePrinter.print_default(mx2)

        print("-" * (mx2.m * 2 + 1))
        self.current_operation = MatrixAddition(mx1, mx2)
        mx_res = self.current_operation.sum(substract = True)
        MatrixConsolePrinter.print_default(mx_res)

    def mx_scal(self):

        print("\nOperace násobení skalárem:")

        print("\nZadání matice:")
        print("¯ ¯ ¯ ¯ ¯ ¯ ¯ ¯")

        mx = self.__read_mx_data(self)


        print("Zadejte skalár:")
        scalar = self.input_reader.read_scalar()

        MatrixConsolePrinter.print_default(mx)
        print("*(",scalar,")", sep="")

        print()

        print("-" * (mx.m * 2 + 1))
        self.current_operation = MatrixScalarMultiplication(mx, scalar)
        mx_res = self.current_operation.multiply()
        MatrixConsolePrinter.print_default(mx_res)

    def mx_multi(self):

        print("\nOperace: Maticové Násobení:")

        print("\nZadání 1. matice:")
        print("¯ ¯ ¯ ¯ ¯ ¯ ¯ ¯ ¯")
        mx1 = self.__read_mx_data(self)

        self.dims_check = lambda sec_mx_dims: Helpers.invalid_dims_multiplication(sec_mx_dims, mx1)

        print("\nZadání 2. matice:")
        print("¯ ¯ ¯ ¯ ¯ ¯ ¯ ¯ ¯")

        mx2 = self.__read_mx_data(self)

        MatrixConsolePrinter.print_default(mx1)
        print("~(*)~")
        MatrixConsolePrinter.print_default(mx2)

        print("-" * (mx2.m * 2 + 1))
        self.current_operation = MatrixMultiplication(mx1, mx2)
        mx_res = self.current_operation.multiply()
        MatrixConsolePrinter.print_default(mx_res)

    def mx_trans(self):
        print("\nOperace: Transpozice:")

        print("\nZadání matice:")
        print("¯ ¯ ¯ ¯ ¯ ¯ ¯ ¯ ¯")
        mx = self.__read_mx_data(self)

        print("-" * (mx.m * 2 + 1))

        self.current_operation = MatrixTransposition(mx)
        mx_res = self.current_operation.transpose()

        MatrixConsolePrinter.print_default(mx_res)

    def mx_ref(self):
        
        print("\nOperace: REF:")

        print("\nZadání matice:")
        print("¯ ¯ ¯ ¯ ¯ ¯ ¯ ¯")
        mx = self.__read_mx_data(self)

        MatrixConsolePrinter.print_default(mx)
        print("~(REF)~")

        print("-" * (mx.m * 2 + 1))

        self.current_operation = MatrixREF(mx)
        mx_res = self.current_operation.matrix_to_ref()

        MatrixConsolePrinter.print_default(mx_res)

    def mx_rref(self):
        print("\nOperace: RREF:")

        print("\nZadání matice:")
        print("¯ ¯ ¯ ¯ ¯ ¯ ¯ ¯")
        mx = self.__read_mx_data(self)

        MatrixConsolePrinter.print_default(mx)
        print("~(RREF)~")

        print("-" * (mx.m * 2 + 1))

        self.current_operation = MatrixRREF(mx)
        mx_res = self.current_operation.matrix_to_rref()
        MatrixConsolePrinter.print_default(mx_res)

        pass

    def mx_inverse(self):

        print("\nOperace: určení inverzní matice:")

        print("\nZadání matice:")
        print("¯ ¯ ¯ ¯ ¯ ¯ ¯ ¯")
        mx = self.__read_mx_data(self)

        MatrixConsolePrinter.print_default(mx)
        print("~(A^(-1))~")

        print("-" * (mx.m**3))

        self.current_operation = MatrixInversion(mx)
        operation_state = self.current_operation.calculate_inversion_of_matrix()

        if operation_state:
            MatrixConsolePrinter.print_default(mx)

    def mx_rank(self):
        print("\n Operace: hodnost matice:")
        
        print("\nZadání matice:")
        print("¯ ¯ ¯ ¯ ¯ ¯ ¯ ¯")
        mx = self.__read_mx_data(self)


        MatrixConsolePrinter.print_default(mx)
        print("~(rank(A))~")

        self.current_operation = MatrixREF(mx)
        mx_res = self.current_operation.matrix_to_ref()

    def mx_det(self):
        print("\n Operace výpočet determinantu:")
 
        print("\nZadání matice:")
        print("¯ ¯ ¯ ¯ ¯ ¯ ¯ ¯")
        mx = self.__read_mx_data(self)

        MatrixConsolePrinter.print_default(mx)
        print("~(det(A))~")


        self.current_operation = MatrixREF(mx)
        self.current_operation.matrix_to_ref()
        determinant = self.current_operation.calculate_determinant()

        print(determinant)

    def mx_pow(self):
        pass
