class Helpers:

    @staticmethod
    def invalid_selection(function_to_repeat):
        print("Hodnota není povolena! Enter – opakujte akci")
        input()
        function_to_repeat() 
