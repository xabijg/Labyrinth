from labyrinth import *

def example1():
    labyrinth1 = [[".",".",".",".",".",".",".",".","."],
                  ["#",".",".",".","#",".",".",".","."],
                  [".",".",".",".","#",".",".",".","."],
                  [".","#",".",".",".",".",".","#","."],
                  [".","#",".",".",".",".",".","#","."]]
    path, steps = solution(labyrinth1)
    print("Resultado 1:", steps," esperado valor: 11")  # 11
    print_labyrinth(labyrinth1, path)
    
def example2():
    labyrinth2 = [[".",".",".",".",".",".",".",".","."],
                  ["#",".",".",".","#",".",".","#","."],
                  [".",".",".",".","#",".",".",".","."],
                  [".","#",".",".",".",".",".","#","."],
                  [".","#",".",".",".",".",".","#","."]]
    path, steps = solution(labyrinth2)
    print("Resultado 2:", steps," esperado valor: -1")  # -1
    print_labyrinth(labyrinth2, path)
def example3():
    labyrinth3 = [[".",".","."],
                  [".",".","."],
                  [".",".","."]]
    path, steps = solution(labyrinth3)
    print("Resultado 3:", steps," esperado valor: 2")  # 2
    print_labyrinth(labyrinth3, path)

def example4():
    labyrinth4 = [[".",".",".",".",".",".",".",".",".","."],
                  [".","#",".",".",".",".","#",".",".","."],
                  [".","#",".",".",".",".",".",".",".","."],
                  [".",".",".",".",".",".",".",".",".","."],
                  [".",".",".",".",".",".",".",".",".","."],
                  [".","#",".",".",".",".",".",".",".","."],
                  [".","#",".",".",".","#",".",".",".","."],
                  [".",".",".",".",".",".","#",".",".","."],
                  [".",".",".",".",".",".",".",".",".","."],
                  [".",".",".",".",".",".",".",".",".","."]]
    path, steps = solution(labyrinth4)
    print("Resultado 4:", steps," esperado valor: 16")  # 16
    print_labyrinth(labyrinth4, path)
