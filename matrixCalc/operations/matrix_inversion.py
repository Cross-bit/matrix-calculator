from operations.matrix_to_ref import MatrixREF
from operations.matrix_to_rref import MatrixRREF
from operations.matrix_determinant import MatrixDeterminant
from operations.elementary_operations import ElementaryOperations
from matrix import Matrix

class MatrixInversion:

    def __init__(self, matrix):
        self.mx = matrix
        self.mx_inv = Matrix(matrix.m, matrix.n)
        self.mx_ref_expanded = None
        self.mx_inv.Data = matrix.Data
        self.__mx_ref_operation = None
        self.__mx_rref_operation = None
        

    def calculate_inversion_of_matrix(self):

        self.mx_ref_expanded = ElementaryOperations.expand_for_identity_matrix(self.mx)
        
        if(self.mx_ref_expanded is None):
            print ("Matice není čtvercová.")
            return

        self.__mx_ref_operation = MatrixREF(self.mx_ref_expanded)
        mx_ref = self.__mx_ref_operation.matrix_to_ref()

        determinant_operation = MatrixDeterminant()
        determinant = determinant_operation.get_determinant(mx_ref, (self.mx.m, self.mx.n), self.__mx_ref_operation.determinant_sign)
        
        if(abs(determinant) < 0.001 ): # menší než 0
            print ("Determinant je nulový, matice nemá inverz.")
            return 

        self.__mx_rref_operation = MatrixRREF(self.mx_ref_expanded)
        self.__mx_rref_operation.pivot_positions = self.__mx_ref_operation.pivot_positions

        self.__mx_rref_operation.matrix_ref_to_rref()
        
        for i in range(0, self.mx_ref_expanded.m):
            self.mx_inv.Data[i] = self.mx_ref_expanded.Data[i][self.mx_inv.n:self.mx_ref_expanded.n]

        return self.mx_inv



        

        
