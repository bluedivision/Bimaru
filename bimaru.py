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

    def __init__(self, matrix, nrow, ncol, count=[1, 2, 3, 4]):
        self.matrix = matrix
        self.nrow = nrow
        self.ncol = ncol
        self.count = count

    def get_value(self, row: int, col: int) -> str:
        return self.matrix[row][col]

    def set_value(self, row: int, col: int, val: str):
        self.matrix[row][col] = val

    def adjacent_vertical_values(self, row: int, col: int) -> (str, str):
        if col > 0:
            up = self.matrix[row - 1][col]
        else:
            up = None
        if col < 9:
            down = self.matrix[row + 1][col]
        else:
            down = None
        return up, down

    def adjacent_horizontal_values(self, row: int, col: int) -> (str, str):
        if row > 0:
            left = self.matrix[row][col - 1]
        else:
            left = None
        if row < 9:
            right = self.matrix[row][col + 1]
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

        # n_hint = int(lines[2])
        # raw_matrix = [lines.split() for line in lines[-n_hint:]]
        raw_matrix = [line.split() for line in lines[3:]]

        matrix = np.full((10, 10), '0')

        for row in raw_matrix:
            # row.pop(0)
            matrix[int(row[1]), int(row[2])] = row[3]

        return Board(matrix, nrow, ncol)

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

    # cuidado com o \n no fim do print

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

        nrow = state.board.nrow
        ncol = state.board.ncol

        action_list = []

        for i in range(10):
            for j in range(10):
                # para cada elemento diferente de '0' e 'W' e 'w', desconta um valor deste elemente em nrow e ncol
                if state.board.matrix[i][j] != '0' and state.board.matrix[i][j] != 'W' and state.board.matrix[i][j] != 'w' and state.board.matrix[i][j] != '.':
                    nrow[i] = nrow[i] - 1
                    ncol[j] = ncol[j] - 1

                    # let '*' represents 'not water'



                    # left actions
                    if state.board.matrix[i][j] == 'L' or state.board.matrix[i][j] == 'l':
                        for m in range(-1,3):
                            if j+m in range(10):
                                if i + 1 in range(10):
                                    action_list.append((i + 1, j + m, 'w'))
                                if i - 1 in range(10):
                                    action_list.append((i - 1, j + m, 'w'))
                                if m == -1:
                                    action_list.append((i, j + m, 'w'))
                                if m == 1:
                                    action_list.append((i, j + m, '*'))

                    # right actions
                    if state.board.matrix[i][j] == 'R' or state.board.matrix[i][j] == 'r':
                        for m in range(-2, 2):
                            if j + m in range(10):
                                if i + 1 in range(10):
                                    action_list.append((i + 1, j + m, 'w'))
                                if i - 1 in range(10):
                                    action_list.append((i - 1, j + m, 'w'))
                                if m == 1:
                                    action_list.append((i, j + m, 'w'))
                                if m == -1:
                                    action_list.append((i, j + m, '*'))

                    # top actions
                    if state.board.matrix[i][j] == 'T' or state.board.matrix[i][j] == 't':
                        for m in range(-1, 3):
                            if i + m in range(10):
                                if j + 1 in range(10):
                                    action_list.append((i + m, j + 1, 'w'))
                                if j - 1 in range(10):
                                    action_list.append((i + m, j - 1, 'w'))
                                if m == -1:
                                    action_list.append((i + m, j, 'w'))
                                if m == 1:
                                    action_list.append((i + m, j, '*'))

                    # bottom actions
                    if state.board.matrix[i][j] == 'B' or state.board.matrix[i][j] == 'b':
                        for m in range(-2, 2):
                            if i + m in range(10):
                                if j + 1 in range(10):
                                    action_list.append((i + m, j + 1, 'w'))
                                if j - 1 in range(10):
                                    action_list.append((i + m, j - 1, 'w'))
                                if m == 1:
                                    action_list.append((i + m, j, 'w'))
                                if m == -1:
                                    action_list.append((i + m, j, '*'))

                    # circle actions
                    if state.board.matrix[i][j] == 'C' or state.board.matrix[i][j] == 'c':
                        for m in (-1, 1):
                            for n in (-1, 1):
                                if i + m in range(10) and j + n in range(10):
                                    action_list.append((i + m, j + n, 'w'))

                    # middle actions
                    if state.board.matrix[i][j] == 'M' or state.board.matrix[i][j] == 'm':
                        for m in (-1, 1):
                            if i + m in range(10):
                                if state.board.matrix[i+m][j] == 'W' or state.board.matrix[i+m][j] == 'w':
                                    for n in range(-2,3):
                                        if j + n in range(10):
                                            action_list.append((i + m, j + n, 'w'))
                                            if i - m in range(10):
                                                action_list.append((i - m, j + n, 'w'))
                                            if n == 1 or n == -1:
                                                action_list.append((i, j + n, '*'))
                                break
                            if j + m in range(10):
                                if state.board.matrix[i][j+m] == 'W' or state.board.matrix[i][j+m] == 'w':
                                    for n in range(-2,3):
                                        if i + n in range(10):
                                            action_list.append((i + n, j + m, 'w'))
                                            if j - m in range(10):
                                                action_list.append((i - n, j + m, 'w'))
                                            if n == 1 or n == -1:
                                                action_list.append((i + n, j, '*'))
                                break


        # water row and column

        for k in range(10):
            if nrow[k] == 0:
                # 10 represents make all the None ('0') values of row(k) equals 'w'
                action_list.append((k, 10, 'w'))
            if ncol[k] == 0:
                # 10 represents make all the None ('0') values of col(k) equals 'w'
                action_list.append((10, k, 'w'))

        # avoiding repeated actions
        unique_list = list(set(action_list))

        return unique_list


    def result(self, state: BimaruState, action):
        """Retorna o estado resultante de executar a 'action' sobre
        'state' passado como argumento. A ação a executar deve ser uma
        das presentes na lista obtida pela execução de
        self.actions(state)."""
        # TODO


        # action(int, int, str)
        # it changes the matrix element [i][j] of the state to the value of str

        i = action[0]
        j = action[1]
        value = action[2]

        if value == 'w':
            value = '.'
        if i != 10 and j != 10:
            state.board.matrix[i][j] = value
        elif i == 10:
            for row in range(10):
                if state.board.matrix[row][j] == '0':
                    state.board.matrix[row][j] = value
        elif j == 10:
            for column in range(10):
                if state.board.matrix[i][column] == '0':
                    state.board.matrix[i][column] = value


        return state

    def goal_test(self, state: BimaruState):
        """Retorna True se e só se o estado passado como argumento é
        um estado objetivo. Deve verificar se todas as posições do tabuleiro
        estão preenchidas de acordo com as regras do problema."""

        nrow1 = state.board.nrow
        ncol1 = state.board.ncol

        for i in range(9):
            test = True
            if nrow1[i] != 0 or ncol1[i] != 0:
                test = False
        return test

    def h(self, node: Node):
        """Função heuristica utilizada para a procura A*."""
        # TODO
        pass

    # TODO: outros metodos da classe


if __name__ == "__main__":
    my_board = Board.parse_instance()
    # verificar se tem barcos. se sim, atualizar o count

    my_board1 = Board(my_board.matrix, my_board.nrow, my_board.ncol, [0, 2, 3, 4])

    print(my_board.matrix)

    my_board.print()
    problem = Bimaru(my_board)


    s0 = BimaruState(my_board)

    # print the list of actions

    print(problem.actions(s0)) #<<<< CORRETO

    act = problem.actions(s0)  #<<<< ERRADO
    print(act)

    # ??????? como podem ser diferentes???


    s1 = problem.result(s0, (5, 10, 'w'))
    print(s1.board.matrix)
    print("\n")
    s2 = problem.result(s1, (10, 1, 'w'))
    print(s2.board.matrix)
    print("\n")

    s3 = problem.result(s2, (10, 2, 'w'))
    print(s3.board.matrix)
    print("\n")

    s4 = problem.result(s3, (10, 3, 'w'))
    print(s4.board.matrix)
    print("\n")

    s5 = problem.result(s4, (10, 5, 'w'))
    print(s5.board.matrix)


    #for x in actions:
    #    s = problem.result(s0, x)

    #print(s.board.matrix)



    # C = np.array([["0" for x in range(10)]for y in range(10)])

    # for i in range(5):
    #    C[i][2] = "T"

    # my_board = Board(C)

    # my_board.print()

    # print(depth_first_tree_search(Bimaru(Board.parse_instance())).state.board)
    # exit(0)

    # TODO:
    # Ler o ficheiro do standard input,
    # Usar uma técnica de procura para resolver a instância,
    # Retirar a solução a partir do nó resultante,
    # Imprimir para o standard output no formato indicado.
