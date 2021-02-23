from matrix import *
from matrix_print.matrix_console_printer import MatrixConsolePrinter as matrix_printer
from input_output.input_reader import *
from main_user_interface import MainUserInterface
from operation_execution import OperationExecution



# Hlavní blok programu
def main_loop():

    user_interface = MainUserInterface()

    # 1)
    operation = user_interface.operation_selection()

    # 2)
    data_load_function = user_interface.data_load_selection()

    # 3)
    operations_executor = OperationExecution(operation, data_load_function)
    operations_executor.execute()
   
    # 4)
    if(operations_executor.operation_result is not None): # Pokud se operace zdařila => nabídka uložení operace
        file_name = user_interface.data_store_selection()
        if file_name:
            operations_executor.write_mx_data_to_file(file_name)

    print()
    return main_loop()

# Začátek programu
main_loop()










