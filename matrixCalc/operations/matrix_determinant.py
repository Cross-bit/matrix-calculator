from operations.matrix_ref import MatrixREF

class MatrixDeterminant:

    def __init__(self, matrix = None):
        self.mx = matrix
        self.determinant = 1

    def calculate_determinant(self):

        matrix_ref_operation = MatrixREF(self.mx)
        mx_ref = matrix_ref_operation.matrix_to_ref()

        return self.get_determinant(mx_ref, determinant_sign = matrix_ref_operation.determinant_sign)


    def get_determinant(self, mx_ref, dimensions = -1, determinant_sign = 0):
        try:
            if dimensions == -1: 
                dimensions = (mx_ref.m, mx_ref.n)


            if dimensions[0] != dimensions[1]:
                print("Matice musí být pro výpočet determinantu čtvercová.")
                return 0.0

            for i in range(dimensions[0]):
                self.determinant *= mx_ref.data[i][i]

            self.determinant *= determinant_sign
            return self.determinant
        except:
            print("Při výpočtu determinantu došlo k chybě!")
            return 0.0
