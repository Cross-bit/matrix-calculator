import sys
from matrix import *
from matrix_print.matrix_console_printer import MatrixConsolePrinter as matrix_printer
from elementary_operations import *
from input_output.input_reader import *
from operations.matrix_multiplication import *
from operations.matrix_transposition import *
from operations.matrix_to_ref import *
from operations.matrix_to_rref import *
from operations.matrix_inversion import *
from operations.matrix_addition import *
from matrix_generator import *
from operation_execution import OperationExecution as OE
from helpers import *
from operations.matrix_scalar_multiplication import MatrixScalarMultiplication

##Testovací matice
#matrix_generator = MatrixGenerator(5,2)

input_r = InputReader()

mx_data = input_r.read_matrix_data_from_file("mxf.txt")

mx = Matrix(len(mx_data), len(mx_data[0]), mx_data);


with open("mx_res.txt", "w") as file:
    file.write('hello world')


        



#from input_output.output_writer import *





#mx = MatrixGenerator.generate_random_matrix(3, 3, 10, 1000_00)

matrix_printer.print_default(mx)


# Hlavní blok programu
def main_loop():
    # 1)
    operation = operation_selection()
    # 2)
    data_load_function = data_load_selection()

    operations_handler = OE(operation, data_load_function)
    operations_handler.execute()

    
    


    print("")
    return main_loop()


# Uživatelské rozhraní výběru operace uživatelem
def operation_selection():
    # Základní výpis dat
    # Separace UI od logiky

    print("Zvolte operaci:\n")
    print("""1) Maticový součet \n2) Maticový rozdíl \n3) Vynásobení skalárem \n4) Mnaticové násobení \n5) Maticová transpozice \n6) Převod na REF \n7) Převod na RREF \n8) Inverzní matice \n9) Určení hodnosti \n10) Určení determinantu 
        """)

    operation_input = input()
    operation_input = operation_input.strip()

    operations = {
        1: OE.mx_add,
        2: OE.mx_sub,
        2: OE.mx_sub,
        3: OE.mx_scal,
        4: OE.mx_multi,
        5: OE.mx_trans,
        6: OE.mx_ref,
        7: OE.mx_rref,
        8: OE.mx_inverse,
        9: OE.mx_rank,
       10: OE.mx_det,
       }
    

    if(operation_input.isnumeric()):
        operation_input = int(operation_input)
        if(operation_input <= len(operations) and operation_input > 0):
            return operations.get(int(operation_input))

    print("Hodnota není povolena! Enter – opakujte akci")
    input()
    return operation_selection()

# Uživatelské rozhraní výběru typu načtení dat
def data_load_selection():
    print("""Vyberte způsob zadání hodnot:\n1) Zadání v konzoli \n2) Načtení ze souboru""")
    try:
        user_selection = input()
        user_selection = int(user_selection.strip())

        if user_selection == 1: #1 z konzole
            return OE.load_data_from_console
        elif user_selection == 2:
            return OE.load_data_from_file
        
        print("Hodnota není povolena! Enter – opakujte akci")
        input()
        return data_load_selection()
    except:
        print("Hodnota není povolena! Enter – opakujte akci")
        input()
        return data_load_selection()

main_loop()


input()
sys.exit
matrix_printer.print_default(mx)

mx.generate_random_values()










