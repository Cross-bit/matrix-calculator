from operation_execution import OperationExecution
from main_user_interface import MainUserInterface
from matrix import Matrix


# Hlavní blok programu
def main_loop():

    user_interface = MainUserInterface()

    # 1) Nabídka volby operace
    operation = user_interface.operation_selection()

    # 2) Volba práce s daty
    data_load_function = user_interface.data_load_selection()

    # 3) Průběh operace
    operations_executor = OperationExecution(operation, data_load_function)
    operations_executor.execute()
   
    # 4) Nabídka uložení výstupních dat do souboru (Pokud se operace zdařila)
    if operations_executor.operation_result is not None:
        file_name = user_interface.data_store_selection()
        if file_name:
            operations_executor.write_mx_data_to_file(file_name)

    print()
    return main_loop()

# Začátek programu
main_loop()










