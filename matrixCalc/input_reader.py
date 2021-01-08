class InputReader:

    def __init__(self, operation_to_read, load_data_from):
        self.input = ""
        self.matrix_dims = ""
        self.expected_operation = operation_to_read
        self.load_data_from = load_data_from

    @staticmethod
    def try_parse_matrix_input(input_data):
        try:
            input_data_arr = input_data.split(" ")
            if(len(input_data_arr) <= 1):
                return [int(input_data_arr)]
            else:
                return list([int(x) for x in input_data_arr])

        #TODO: Vracení chybových hlášek
        except:
            return False

    def read_matrix_dimensions(self):
        continue_reading = True
        while(continue_reading):
            if(self.expected_operation):
                pass
            else:
               return dimensions
    
    def read_matrix_data(self):



    def read_matrix_user_input(self):
        ctr = 0
        while(ctr < mx.m):
            continue_read_row = True

            # Čtení řádky
            while(continue_read_row):
                input_row = input()
                parsed_data_arr = try_parse_matrix_input(input_row)
                if(parsed_data_arr and len(parsed_data_arr) == mx.n):
                    mx.Data[ctr] = parsed_data_arr
                    continue_read_row = False
                else:
                    print("Neplatně zadaný řádek matice, zkuste to prosím znovu: ")
                    if(ctr > 0):
                        matrix_printer.print_simple(mx)
            ctr += 1

    def load_matrix_data_from_file(self, file_name):
        f = open()



    def try_parse_matrix_dims(dim_string):
        try:
            dimensions = list([int(x) for x in dim_string.split("x")])
            
            if(dimensions != 2):
                return False
            return dimensions

        except:
            return False



