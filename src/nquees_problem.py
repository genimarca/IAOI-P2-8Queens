'''
Created on 30 nov. 2022

@author: Eugenio Martínez Cámara
'''

import random

from search import NQueensProblem, depth_first_graph_search, hill_climbing,\
    depth_first_tree_search, hill_climbing_min, breadth_first_tree_search, simulated_annealing


def print_result(tlabel, x):
    
    print(tlabel+"\n")
    
    
    board = [["0"]*len(x) for i in range(len(x))]
    for c,r in enumerate(x):
        board[r][c] = "1"
    
    print("\n".join(" ".join(row) for row in board))


if __name__ == '__main__':
    
    random.seed(7) #To make reproducible
    
    problem = NQueensProblem(8)
    depth_result = depth_first_tree_search(problem)
    print_result("Profundidad", depth_result.state)
    breadth_result=breadth_first_tree_search(problem)
    print_result("Anchura", depth_result.state)
    hill_result = hill_climbing_min(problem)
    print()
    print_result("Hill", hill_result)
    ann_result = simulated_annealing(problem)
    print_result("Simulated", ann_result)
    
    
    
    
    
    