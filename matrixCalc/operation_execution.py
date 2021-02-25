from operations.matrix_addition import MatrixAddition 
from operations.matrix_determinant import MatrixDeterminant
from operations.matrix_inversion import MatrixInversion
from operations.matrix_ref import MatrixREF
from operations.matrix_rref import MatrixRREF
from operations.matrix_transposition import MatrixTransposition
from operations.matrix_scalar_multiplication import MatrixScalarMultiplication
from operations.matrix_multiplication import MatrixMultiplication
from elementary_operations import ElementaryOperations

from matrix import Matrix
from helpers import Helpers
from matrix_print.matrix_console_printer import MatrixConsolePrinter
from input_output.input_reader import InputReader
from input_output.output_writer import OutputWriter
import constants


class OperationExecution:
    """Stará se o průběh a exekuci operací kalkulačky."""

    def __init__(self, mx_operation_method, load_data_method):

        self.__read_mx_data = load_data_method;
        self.__operation = mx_operation_method; # Pointer na metodu zprostředkující danou operaci 

        self.input_reader = InputReader()
        self.output_writer = OutputWriter()

        self.__current_operation = None # Reference objektu momentální operace z modulu operations
        self.operation_result = None

        # Funkce sloužící ke kontrole rozměrů matice při zadávání hodnot uživatelem
        self.dims_check = lambda x: True 

    def execute(self):
        self.__operation(self);

    def write_result_to_file(self, file_name):
        if(file_name == ""): raise Exception("Název souboru je prázdný!")
        if(self.operation_result is None): raise Exception("Výsledek operace je neplatný!")
        self.output_writer.store_output(self.operation_result, file_name)
            

    def __get_mx_dims_console(self):
        print("Zadejte rozměry matice celými čísly, ve tvaru: mxn \n(tedy např. 2x2):")
        return self.input_reader.read_matrix_dimensions(self.dims_check)

    def load_data_from_file(self):

        print("Zadejte název cílového souboru ve formátu .txt (stačí bez přípony):")
        data_file_name = input()

        mx_data = self.input_reader.read_matrix_data_from_file(data_file_name);

        if mx_data:
            mx = Matrix(len(mx_data), len(mx_data[0]), mx_data)
            dims = (mx.m, mx.n)

            if self.dims_check(dims):
                return mx
            else:
                print("Rozměry matice jsou neplatné, zkuste prosím jiný soubor:")


        return self.load_data_from_file();

    def load_data_from_console(self):
        dims = self.__get_mx_dims_console()
        mx = Matrix(dims[0], dims[1])

        print("\nZadejte hodnoty matice po řádcích oddělné mezerou:")
        self.input_reader.read_matrix_user_input(mx)

        return mx            

    def mx_add(self):
        #1)
        print("\nOperace sčítání:")
        #2)
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

        print(" - " * (mx2.m * 2))
        self.__current_operation = MatrixAddition(mx1, mx2)
        self.operation_result = self.__current_operation.calculate_sum()
        MatrixConsolePrinter.print_default(self.operation_result)

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

        print(" - " * (mx2.m * 2 ))
        self.__current_operation = MatrixAddition(mx1, mx2)
        self.operation_result = self.__current_operation.calculate_sum(substract = True)
        MatrixConsolePrinter.print_default(self.operation_result)

    def mx_scalar_multiply(self):

        print("\nOperace násobení skalárem:")

        print("\nZadání matice:")
        print("¯ ¯ ¯ ¯ ¯ ¯ ¯ ¯")

        mx = self.__read_mx_data(self)


        print("Zadejte skalár:")
        scalar = self.input_reader.read_scalar()

        MatrixConsolePrinter.print_default(mx)
        print("*(",scalar,")", sep="")


        print(" - " * (mx.m * 2))
        self.__current_operation = MatrixScalarMultiplication(mx, scalar)
        self.operation_result = self.__current_operation.calculate_scalar_multiplication()
        MatrixConsolePrinter.print_default(self.operation_result)

    def mx_multiply(self):

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

        print(" - " * (mx2.m * 2))
        self.__current_operation = MatrixMultiplication(mx1, mx2)
        self.operation_result = self.__current_operation.calculate_multiplication()
        MatrixConsolePrinter.print_default(self.operation_result)

    def mx_transpose(self):
        print("\nOperace: Transpozice:")

        print("\nZadání matice:")
        print("¯ ¯ ¯ ¯ ¯ ¯ ¯ ¯ ¯")
        mx = self.__read_mx_data(self)

        MatrixConsolePrinter.print_default(mx)
        print("~(A^(T))~")
        print(" - " * (mx.m * 2))

        self.__current_operation = MatrixTransposition(mx)
        self.operation_result = self.__current_operation.calculate_transpose()

        MatrixConsolePrinter.print_default(self.operation_result)

    def mx_ref(self):
        
        print("\nOperace: REF:")

        print("\nZadání matice:")
        print("¯ ¯ ¯ ¯ ¯ ¯ ¯ ¯")
        mx = self.__read_mx_data(self)

        MatrixConsolePrinter.print_default(mx)
        print("~(REF)~")

        print(" - " * (mx.m * 2))

        self.__current_operation = MatrixREF(mx)
        self.operation_result = self.__current_operation.calculate_ref()

        MatrixConsolePrinter.print_default(self.operation_result)

    def mx_rref(self):
        print("\nOperace: RREF:")

        print("\nZadání matice:")
        print("¯ ¯ ¯ ¯ ¯ ¯ ¯ ¯")
        mx = self.__read_mx_data(self)

        MatrixConsolePrinter.print_default(mx)
        print("~(RREF)~")

        print(" - " * (mx.m * 2))

        self.__current_operation = MatrixRREF(mx)
        self.operation_result = self.__current_operation.calculate_rref()
        MatrixConsolePrinter.print_default(self.operation_result)

    def mx_inverse(self):

        print("\nOperace: určení inverzní matice:")

        print("\nZadání matice:")
        print("¯ ¯ ¯ ¯ ¯ ¯ ¯ ¯")
        mx = self.__read_mx_data(self)

        MatrixConsolePrinter.print_default(mx)
        print("~(A^(-1))~")

        print(" - " * (mx.m * 2))

        self.__current_operation = MatrixInversion(mx)
        self.operation_result = self.__current_operation.calculate_inversion_of_matrix()

        if self.__current_operation.inversion_state:
            MatrixConsolePrinter.print_default(self.operation_result)

    def mx_rank(self):
        print("\n Operace: hodnost matice:")
        
        print("\nZadání matice:")
        print("¯ ¯ ¯ ¯ ¯ ¯ ¯ ¯")
        mx = self.__read_mx_data(self)


        MatrixConsolePrinter.print_default(mx)
        print("~(rank(A))~")

        self.__current_operation = MatrixREF(mx)
        mx_res = self.__current_operation.calculate_ref()
        self.operation_result = self.__current_operation.rank
        print(self.operation_result)

    def mx_determinant(self):
        print("\n Operace výpočet determinantu:")
 
        print("\nZadání matice:")
        print("¯ ¯ ¯ ¯ ¯ ¯ ¯ ¯")
        mx = self.__read_mx_data(self)

        MatrixConsolePrinter.print_default(mx)
        print("~(det(A))~")


        self.__current_operation = MatrixDeterminant(mx);
        self.operation_result = self.__current_operation.calculate_determinant()

        print(self.operation_result)
