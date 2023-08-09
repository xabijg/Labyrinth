from labyrinth import *

def example1():
    labyrinth1 = [[".",".",".",".",".",".",".",".","."],
                  ["#",".",".",".","#",".",".",".","."],
                  [".",".",".",".","#",".",".",".","."],
                  [".","#",".",".",".",".",".","#","."],
                  [".","#",".",".",".",".",".","#","."]]
    return solution(labyrinth1)

def example2():
    labyrinth2 = [[".",".",".",".",".",".",".",".","."],
                  ["#",".",".",".","#",".",".","#","."],
                  [".",".",".",".","#",".",".",".","."],
                  [".","#",".",".",".",".",".","#","."],
                  [".","#",".",".",".",".",".","#","."]]
    return solution(labyrinth2)

def example3():
    labyrinth3 = [[".",".","."],
                  [".",".","."],
                  [".",".","."]]
    return solution(labyrinth3)

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
    return solution(labyrinth4)
