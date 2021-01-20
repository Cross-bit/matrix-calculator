from operations import *

class InputReader:

    def __init__(self, load_data_from):
        self.input = ""
        self.matrix_dims = ""
        self.load_data_from = load_data_from

    def try_parse_matrix_input(self, input_data):
        try:
            input_data_arr = input_data.split(" ")
            if(len(input_data_arr) <= 1):
                return [int(input_data_arr)]
            else:
                return list([int(x) for x in input_data_arr])
        #TODO: Vracení chybových hlášek
        except:
            return False

    def read_matrix_dimensions(self, validity_condition):
        """ 
        check_if_valid – Očekává funkci typu: lambda x: True/False
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

            # Čtení řádky
            while(continue_read_row):
                input_row = input()
                parsed_data_arr = self.try_parse_matrix_input(input_row)
                if(parsed_data_arr and len(parsed_data_arr) == mx.n):
                    mx.Data[ctr] = parsed_data_arr
                    continue_read_row = False
                else:
                    print("Neplatně zadaný řádek matice, zkuste to znovu: ")
                    if(ctr > 0):
                        matrix_printer.print_simple(mx, formated = False)
            ctr += 1

    def read_scalar(self):
        scalar = 0
        try:
            scalar = input()
            if(scalar.isnumeric()):
                return int(scalar)
            else:
                print("Neplatně zadaný skalár, zkuste to znovu: ")
                return self.read_scalar()

        except:
            return self.read_scalar()



    def load_matrix_data_from_file(self, file_name, num_of_matrixes):
        f = open("file_name", "r")
        mx_raw_data = f.read()
        # first row dims



    def __try_parse_matrix_dims(self, dim_string):
        try:
            dimensions = list([int(x) for x in dim_string.split("x")])
            
            if(len(dimensions) != 2):
                return False
            return dimensions
        except:
            return False



