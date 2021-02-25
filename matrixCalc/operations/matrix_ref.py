from elementary_operations import ElementaryOperations
from matrix import Matrix
import constants

class MatrixREF:

    def __init__(self, matrix):
        self.mx = matrix
        self.mx_ref = Matrix(matrix.m, matrix.n, matrix.data)
        self.rank = 0
        self.pivot_positions = []
        self.determinant = 1.0
        self.determinant_sign = 1

    def calculate_ref(self):

        pivot_i_position = 0 # pozice v řádku
        pivot_j_position = 0 # pozice v sloupci

        while pivot_j_position < self.mx.n and pivot_i_position < self.mx.m:
            
            # Pokud je pivot 0, tak je nutné prohodit řádky
            if abs(self.mx_ref.data[pivot_i_position][pivot_j_position]) < 10.0**(constants.OUTPUT_PRECISION*(-1)):
                new_pivot_pos = ElementaryOperations.find_first_most_left_value(self.mx_ref, pivot_i_position, pivot_j_position)
                # Už nejsou další pivoty, matice je odstupňovaná
                if not self.__check_if_pivot_position_is_valid(new_pivot_pos):
                    return self.mx_ref

                pivot_j_position = new_pivot_pos[1]

                # prohození řádků
                ElementaryOperations.exchange_rows(self.mx_ref, pivot_i_position, int(new_pivot_pos[0]))

                self.determinant_sign *= -1 # Pro determinant se obrátí znaménko

            self.__calculate_ref_for_pivot_row(pivot_i_position, pivot_j_position)

            self.pivot_positions.append([pivot_i_position, pivot_j_position])
            
            pivot_j_position += 1
            pivot_i_position += 1

        self.rank = len(self.pivot_positions)

        return Matrix(self.mx.m, self.mx.n, self.mx_ref.data)
    
    def __check_if_pivot_position_is_valid(self, pivot_pos):
        return (pivot_pos[0] != 0 or pivot_pos[1] != 0)

    def __calculate_ref_for_pivot_row(self, pivot_i_position, pivot_j_position):
        for i in range(pivot_i_position+1, self.mx.m):
            multiply_const = (-1)*self.mx_ref.data[i][pivot_j_position] / self.mx_ref.data[pivot_i_position][pivot_j_position]

            for c in range(pivot_j_position, self.mx.n): # Přičtení násobku řádku
                self.mx_ref.data[i][c] = self.mx_ref.data[i][c] + self.mx_ref.data[pivot_i_position][c] * multiply_const            


            







                    

                

                

