class Helpers:

    @staticmethod
    def invalid_selection(function_to_repeat):
        print("Hodnota není povolena! Enter – opakujte akci")
        input()
        return function_to_repeat() 


    @staticmethod
    def invalid_dims_addition(sec_mx_dims, mx):
        """
        sec_mx_dims: Rozměry matice(v podobě pole: [m, n]; m – počet řádků, n – počet sloupců matice)
        mx: Porovnávaná matice
        """
        is_valid = bool(sec_mx_dims[0] == mx.m and sec_mx_dims[1] == mx.n)
        if not (is_valid):
            print("Rozměry matic při sčítání/odčítání se musejí shodovat!")
        return is_valid

    @staticmethod
    def invalid_dims_multiplication(sec_mx_dims, mx):
        """
        sec_mx_dims: Rozměry matice(v podobě pole: [m, n]; m – počet řádků, n – počet sloupců matice)
        mx: Porovnávaná matice
        """
        is_valid = bool(sec_mx_dims[0] == mx.m)
        if not (is_valid):
            print("Počet sloupců první matice se v součinu musí rovnat počtu řádků druhé!")
        return is_valid



