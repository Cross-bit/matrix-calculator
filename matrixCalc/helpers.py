class Helpers:

    @staticmethod
    def invalid_selection(function_to_repeat):
        print("Hodnota není povolena! Enter – opakujte akci")
        input()
        return function_to_repeat() 


    @staticmethod
    def invalid_dims_addition(second_mx_dims, matrix): 
        """
        sec_mx_dims: Rozměry matice(v podobě pole: [m, n]; m – počet řádků, n – počet sloupců matice)
        mx: Porovnávaná matice
        """
        is_valid = bool(second_mx_dims[0] == matrix.m and second_mx_dims[1] == matrix.n)
        if not (is_valid):
            print("Rozměry matic při sčítání/odčítání se musejí shodovat!")
        return is_valid

    @staticmethod
    def invalid_dims_multiplication(second_mx_dims, matrix):
        """
        sec_mx_dims: Rozměry matice(v podobě pole: [m, n]; m – počet řádků, n – počet sloupců matice)
        mx: Porovnávaná matice
        """
        is_valid = bool(second_mx_dims[0] == matrix.n)
        if not (is_valid):
            print("Počet sloupců první matice se v součinu musí rovnat počtu řádků druhé!")
        return is_valid

    @ staticmethod 
    def correnct_file_name_exstention(file_name, valid_exstention = "txt"):
        return file_name if file_name.endswith(valid_exstention) else "{0}.{1}".format(file_name, valid_exstention);


