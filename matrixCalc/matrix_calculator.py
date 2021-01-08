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

print("1) Sečti matice")
print("2) Odečti matice")
print("3) Vynásob skalárem")
print("4) Vynásob mnatice")
print("5) Transponuj matici")
print("6) Převeď na REF")
print("7) Převeď to RREF")
print("8) Urči inverzní matici")
print("9) Urči hodnost")
print("10) Urči determinant")

operation = input()

print("Vyber způsob zadání hodnot:")
print("1) zadání do konzole")
print("2) načtení ze souboru")
data_input = input()

input_readr = InputReader()



mx = Matrix(2, 5)
mx2 = Matrix(2, 2)
mx = matrix_generator.get_test_matrix_3x3_2()

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










