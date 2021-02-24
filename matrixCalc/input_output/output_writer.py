from matrix_print.matrix_console_printer import MatrixConsolePrinter
from matrix import Matrix
from helpers import Helpers
import constants
import os


class OutputWriter:

    def store_output(self, data_to_print, file_name):
        file_name = Helpers.correnct_file_name_exstention(file_name)
        output_file_path  = '{0}/../{1}/{2}'.format(os.path.dirname(__file__), constants.OUTPUT_FILES_DIR, file_name)
        self.__write_data(data_to_print, output_file_path)

    def __write_data(self, data_to_print, path_to_file):
        try:
            data_string = ''
            if type(data_to_print) is Matrix:
                data_string = MatrixConsolePrinter.print_simple(data_to_print, get = True)
            else:
                data_string = str(data_to_print)

            with open(path_to_file, 'w') as file:
                file.write(data_string)
        except:
            print('Při zápisu souboru došlo k chybě.')

        







