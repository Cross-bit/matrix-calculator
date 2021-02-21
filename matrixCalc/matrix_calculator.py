import sys
from matrix import *
from matrix_print.matrix_console_printer import MatrixConsolePrinter as matrix_printer
from input_output.input_reader import *
from operations.matrix_addition import *
from matrix_generator import *
from operation_execution import OperationExecution as OE


#input_r = InputReader()
#mx_data = input_r.read_matrix_data_from_file("mxf.txt")
#mx = Matrix(len(mx_data), len(mx_data[0]), mx_data);
#đmatrix_printer.print_default(mx)


# Hlavní blok programu
def main_loop():
    # 1)
    operation = operation_selection()
    # 2)
    data_load_function = data_load_selection()

    operations_executor = OE(operation, data_load_function)
    operations_executor.execute()
   
    data_store_selection()

    print()
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
       10: OE.mx_determinant,
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

# Uživatelské rozhraní uložení dat
def data_store_selection():
    print("""Pokud si přejete matici uložit napiště jmémo souboru, nebo pro pokračování stiskněte Enter""")

    try:
        user_input = input()
        user_input = user_input.strip()
        if(user_input == ""):
            return False
        
    except:
        print("""Název souboru není platný, zkuste to prosím znovu:""")
        return data_store_selection()


# Začátek programu
main_loop()










