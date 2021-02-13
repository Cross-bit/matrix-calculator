from operations import *

class InputReader:

    def __init__(self, load_data_from):
        self.input = ""
        self.matrix_dims = ""
        self.load_data_from = load_data_from #TODO: odstranit

    def __try_parse_matrix_input(self, input_data):
        try:
            input_data_arr = input_data.split(" ")
            return list([float(x) for x in input_data_arr])
        except:
            return False

    def read_matrix_dimensions(self, validity_condition):
        """ 
        check_if_valid – Očekává funkci jako: lambda x: True/False
        """
        continue_reading = True

        dimensions = []
        try:
            dimensions = self.__try_parse_matrix_dims(input())

            if dimensions == False or validity_condition(dimensions) == False:
                print("Neplatně zadané rozměry matice, zkuste to znovu:")
                return self.read_matrix_dimensions(validity_condition)
            else:
                return dimensions
        except:
            print("Neplatně zadané rozměry matice, zkuste to znovu:")
            return self.read_matrix_dimensions(validity_condition)

    def read_matrix_user_input(self, mx):
        ctr = 0

        while(ctr < mx.m):
            continue_read_row = True

            # Čtení řádku
            while(continue_read_row):
                input_row = input()
                parsed_data_arr = self.__try_parse_matrix_input(input_row)
                if(parsed_data_arr and len(parsed_data_arr) == mx.n):
                    mx.Data[ctr] = parsed_data_arr
                    continue_read_row = False
                else:
                    print("Neplatně zadaný řádek matice, zkuste to znovu: ")
                    if(ctr > 0):
                        matrix_printer.print_simple(mx, formated = False)
            ctr += 1

    def read_scalar(self):
        """
        Vrátí skalár zadaný v konzoli jako typ float.
        """
        scalar = 0
        try:
            scalar = input()
            if(scalar.isnumeric()):
                return float(scalar)
            else:
                print("Neplatně zadaný skalár, zkuste to znovu: ")
                return self.read_scalar()

        except:
            return self.read_scalar()

    def read_matrix_data_from_file(self, file_name):

        try:
            mx_data_arr = []

            f = open(file_name, "r")
            mx_raw_data = [];

            i = 0
            for line in f.readlines():
                if line.strip():
                    mx_data_arr.append([float(val) for val in line.split()])
                    i += 1
            f.close()

            return mx_data_arr
        except:
            print("Načtení matice ze souboru se nezdařilo.")
            return False

    def __try_parse_matrix_dims(self, dim_string):
        try:
            dimensions = list([int(x) for x in dim_string.split("x")])
            
            if(len(dimensions) != 2 or dimensions[0] < 1 or dimensions[1] < 1):
                return False
            return dimensions
        except:
            return False


