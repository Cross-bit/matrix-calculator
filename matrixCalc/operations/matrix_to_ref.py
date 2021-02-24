from operations.elementary_operations import ElementaryOperations
from matrix import Matrix


class MatrixREF:

    def __init__(self, matrix):
        self.mx = matrix
        self.mx_ref = Matrix(matrix.m, matrix.n, matrix.Data)
        self.rank = 0
        self.pivot_positions = []
        self.determinant = 1.0
        self.determinant_sign = 1

    def matrix_to_ref(self):

        pivot_i_position = 0 # pozice v řádku
        pivot_j_position = 0 # pozice v sloupci

        while (pivot_j_position < self.mx.n and pivot_i_position < self.mx.m):
            
            # Pokud je pivot 0, tak je nutné prohodit řádky
            if(self.mx_ref.Data[pivot_i_position][pivot_j_position] == 0):
                new_pivot_pos = ElementaryOperations.find_first_most_left_value(self.mx_ref, pivot_i_position, pivot_j_position)
                # Už nejsou další pivoty, matice je odstupňovaná
                if not self.__check_if_pivot_position_is_valid(new_pivot_pos):
                    return self.mx_ref

                pivot_j_position = new_pivot_pos[1]
                # prohození řádků
                self.__switch_zero_pivot_row(pivot_i_position, int(new_pivot_pos[0])) 

                self.determinant_sign *= -1 # Pro determinant se obrátí znaménko

            self.__calculate_ref_for_pivot_row(pivot_i_position, pivot_j_position)

            self.pivot_positions.append([pivot_i_position, pivot_j_position])
            
            pivot_j_position += 1
            pivot_i_position += 1

        self.rank = len(self.pivot_positions)

        return Matrix(self.mx.m, self.mx.n, self.mx_ref.Data)
    
    def __check_if_pivot_position_is_valid(self, pivot_pos):
        return (pivot_pos[0] != 0 or pivot_pos[1] != 0)

    def __switch_zero_pivot_row(self, pivot_i_position, new_pivot_i_position):
        ElementaryOperations.exchange_rows(self.mx_ref, pivot_i_position, new_pivot_i_position)

    def __calculate_ref_for_pivot_row(self, pivot_i_position, pivot_j_position):
        for i in range(pivot_i_position+1, self.mx.m):
            multiply_const = (-1)*self.mx_ref.Data[i][pivot_j_position] / self.mx_ref.Data[pivot_i_position][pivot_j_position]

            for s in range(pivot_j_position, self.mx.n): # Přičtení násobku řádku
                self.mx_ref.Data[i][s] = self.mx_ref.Data[i][s] + self.mx_ref.Data[pivot_i_position][s] * multiply_const            


            







                    

                

                

