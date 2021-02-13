from matrix import *
from elementary_operations import *
from matrix_console_printer import MatrixConsolePrinter as matrix_printer
from operations.matrix_to_ref import *


class MatrixRREF:

    def __init__(self, matrix):
        self.mx = matrix
        self.mx_rref = Matrix(matrix.m, matrix.n)
        self.mx_rref.Data = matrix.Data
        self.pivot_positions = []
        self.rank = 0
        self.__matrix_ref = None


    
    def matrix_to_rref(self):

        # Vypočítá se standardní REF
        self.__matrix_ref = MatrixREF(self.mx)
        self.mx_rref = self.__matrix_ref.matrix_to_ref()
        self.pivot_positions = self.__matrix_ref.pivot_positions
        

        # Zpětný průchod maticí pro získání RREF tvaru
        self.matrix_ref_to_rref()

        return self.mx_rref


    def matrix_ref_to_rref(self):

        # edgeCase pivot pouze v prvním řádku nebo se jedná o číslo
        if len(self.pivot_positions) == 1:
            ElementaryOperations.multiply_row_by_scalar(self.mx, 0, 1/self.mx_rref.Data[0][0])
            return

        # Stačí projít všechny sloupce obsahující pivot
        for pivot_pos in reversed(self.pivot_positions):

            # Projdu řádky od i-té pozice pivota až k prvnímu řádku
            for i in range(pivot_pos[0]-1, -1, -1):
               # print(pivot_pos,":",self.mx_rref.Data[i])
                pivot_val = self.mx_rref.Data[pivot_pos[0]][pivot_pos[1]] 

                multiply_const = (-1) * self.mx_rref.Data[i][pivot_pos[1]]/pivot_val

                # Přičtu násobek(stačí průchod od pozice pivota)
                for j in range(pivot_pos[1], self.mx_rref.n):
                    self.mx_rref.Data[i][j] += self.mx_rref.Data[pivot_pos[0]][j] * multiply_const
                    self.mx_rref.Data[pivot_pos[0]][j] /= pivot_val # normalizuji pivot

                # Normalizuji dodatečně první řádek
                ElementaryOperations.multiply_row_by_scalar(self.mx, 0, 1/self.mx_rref.Data[0][0])



