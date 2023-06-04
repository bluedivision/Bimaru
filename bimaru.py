# bimaru.py: Template para implementação do projeto de Inteligência Artificial 2022/2023.
# Devem alterar as classes e funções neste ficheiro de acordo com as instruções do enunciado.
# Além das funções e classes já definidas, podem acrescentar outras que considerem pertinentes.

# Grupo 155:
# 94774 Víctor Liotti
# 99435 Miguel Salvador

import sys
import numpy as np

from search import (
    Problem,
    Node,
    astar_search,
    breadth_first_tree_search,
    depth_first_tree_search,
    greedy_search,
    recursive_best_first_search,
)
import numpy as np

class BimaruState:
    state_id = 0

    def __init__(self, board):
        self.board = board
        self.id = BimaruState.state_id
        BimaruState.state_id += 1

    def __lt__(self, other):
        return self.id < other.id

    # TODO: outros metodos da classe


class Board:
    """Representação interna de um tabuleiro de Bimaru."""
    def __init__(self,matrix):
        self.matrix = matrix

    def get_value(self, row: int, col: int) -> str:
        return self.matrix[row][col]

    def adjacent_vertical_values(self, row: int, col: int) -> (str, str):
        if col > 0:
            up = self.matrix[row-1][col]
        else:
            up = None
        if col < 9:
            down = self.matrix[row+1][col]
        else:
            down = None
        return up, down

    def adjacent_horizontal_values(self, row: int, col: int) -> (str, str):
        if row > 0:
            left = self.matrix[row][col-1]
        else:
            left = None
        if row < 9:
            right = self.matrix[row][col+1]
        else:
            right = None
        return left, right

    @staticmethod
    def parse_instance():

        """Lê o test do standard input (stdin) que é passado como argumento
        e retorna uma instância da classe Board.

        Por exemplo:
            $ python3 bimaru.py < input_T01

            > from sys import stdin
            > line = stdin.readline().split()
        """
        
        from sys import stdin
        
        lines = stdin.readlines()
        
        nrow = []
        ncol = []
        
        line1 = lines[0].split()
        nrow = [int(x) for x in line1[1:]]
        line2 = lines[1].split()
        ncol = [int(y) for y in line2[1:]]
        
        #n_hint = int(lines[2])
        #raw_matrix = [lines.split() for line in lines[-n_hint:]]
        raw_matrix = [line.split() for line in lines[3:]]
        
        
        matrix = np.full((10,10),'0')
        
        for row in raw_matrix:
            #row.pop(0)
            matrix[int(row[1]),int(row[2])] = row[3]
            
        return matrix, nrow, ncol

##############################
    
    def print(self):
        a = ""
        for i in range(10):
            for j in range(10):
                if self.matrix[i][j] == "0":
                    a = a + "."
                else:
                    a = a + self.matrix[i][j]
            a = a + "\n"
        print(a)

    # TODO: outros metodos da classe


class Bimaru(Problem):
    def __init__(self, board: Board):
        self.initial_state = BimaruState(board)
        """O construtor especifica o estado inicial."""
        # TODO
        pass

    def actions(self, state: BimaruState):
        """Retorna uma lista de ações que podem ser executadas a
        partir do estado passado como argumento."""
        # TODO
        pass

    def result(self, state: BimaruState, action):
        """Retorna o estado resultante de executar a 'action' sobre
        'state' passado como argumento. A ação a executar deve ser uma
        das presentes na lista obtida pela execução de
        self.actions(state)."""
        # TODO
        pass

    def goal_test(self, state: BimaruState):
        """Retorna True se e só se o estado passado como argumento é
        um estado objetivo. Deve verificar se todas as posições do tabuleiro
        estão preenchidas de acordo com as regras do problema."""
        # TODO
        pass

    def h(self, node: Node):
        """Função heuristica utilizada para a procura A*."""
        # TODO
        pass

    # TODO: outros metodos da classe


if __name__ == "__main__":

    from sys import stdin
    line = stdin.readline().split()
    print(line)



    f = open("instance01.txt", "r")
    contents = f.read()
    print(contents)

    C = np.array([["0" for x in range(10)]for y in range(10)])

    for i in range(5):
        C[i][2] = "T"

    my_board = Board(C)

    my_board.print()

    # TODO:
    # Ler o ficheiro do standard input,
    # Usar uma técnica de procura para resolver a instância,
    # Retirar a solução a partir do nó resultante,
    # Imprimir para o standard output no formato indicado.
    pass
