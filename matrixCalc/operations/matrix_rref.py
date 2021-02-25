from matrix import Matrix
from elementary_operations import ElementaryOperations
from operations.matrix_ref import MatrixREF
from operations.matrix_determinant import MatrixDeterminant
import constants

class MatrixRREF:

    def __init__(self, matrix):
        self.mx = matrix
        self.mx_rref = Matrix(matrix.m, matrix.n, matrix.data) 
        self.pivot_positions = []
        self.rank = 0
        self.__matrix_ref = None
    

    def calculate_rref(self):

        # Převod na standardní REF
        self.__matrix_ref = MatrixREF(self.mx)

        self.mx_rref = self.__matrix_ref.calculate_ref()
        self.pivot_positions = self.__matrix_ref.pivot_positions
        

        # Zpětný průchod maticí pro získání RREF tvaru
        self.matrix_ref_to_rref()
         
        return self.mx_rref

    def matrix_ref_to_rref(self):

        # edgecase pivot pouze v prvním řádku nebo se jedná o číslo
        if len(self.pivot_positions) == 1:
            if(self.mx_rref.data[0][self.pivot_positions[0][1]] != 0):
                ElementaryOperations.multiply_row_by_scalar(self.mx, 0, 1/self.mx_rref.data[0][self.pivot_positions[0][1]])
            return
        if len(self.pivot_positions) == 0:
            return
        
        # Stačí projít všechny sloupce obsahující pivot
        for pivot_pos in reversed(self.pivot_positions):

            # Projdu řádky od i-té pozice pivota až k prvnímu řádku
            for i in range(pivot_pos[0]-1, -1, -1):

                pivot_val = self.mx_rref.data[pivot_pos[0]][pivot_pos[1]] 

                multiply_const = (-1) * self.mx_rref.data[i][pivot_pos[1]]/pivot_val
                
                # Přičtu násobek (stačí průchod od pozice pivot_pos[1])
                for j in range(pivot_pos[1], self.mx_rref.n):
                    self.mx_rref.data[i][j] += self.mx_rref.data[pivot_pos[0]][j] * multiply_const
                    self.mx_rref.data[pivot_pos[0]][j] /= pivot_val # normalizuji pivot
            
        # Normalizuji dodatečně první řádek
        if abs(self.mx_rref.data[0][self.pivot_positions[0][1]]) > 10.0**(constants.OUTPUT_PRECISION*(-1)):
            ElementaryOperations.multiply_row_by_scalar(self.mx, 0, 1/self.mx_rref.data[0][self.pivot_positions[0][1]])

