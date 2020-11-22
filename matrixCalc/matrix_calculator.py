import sys
from matrix import *
from matrix_console_printer import MatrixConsolePrinter as matrix_printer
from elementary_operations import *
from input_reader import *
from operations.matrix_multiplication import *
from operations.matrix_transposition import *
from operations.matrix_to_ref import *
from matrix_generator import *

#Testovací matice
matrix_generator = MatrixGenerator(5,2)

mx = Matrix(2, 5)
mx2 = Matrix(2, 2)
mx2.generate_random_values()
mx.generate_random_values()


matrix_printer.print_default(mx)
matrix_printer.matrix_to_bracket_string(mx)
matrix_ref_operation = MatrixREF(mx)

mx_ref = matrix_ref_operation.convert_matrix_to_ref()
matrix_printer.print_default(mx_ref)



input()
sys.exit

#TODO: Doimplementuji později(rozpracováno ve třídě input_reader)
operation = input("Vyberte maticovou operaci:\n")
if(operation == 1):
    pass


print("Zadejte rozměry matice v podobě nxm (tedy např. 3x3)")

print("Vložte hodnoty řádků matice {0}x{1} (symboly oddělujte mezerou):".format(mx.n, mx.m))



matrix_printer.print_default(mx)


mx.generate_random_values()










