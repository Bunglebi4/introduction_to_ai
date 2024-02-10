import collections
from copy import deepcopy
from collections import deque

START_STATE = [[6, 2, 8], [4, 1, 7], [5, 3, 0]]
TARGET_STATE = [[0, 1, 2], [3, 4, 5], [6, 7, 8]]

#Класс узла
class Node:
    def __init__(self, action: str, parent=None, cost=0, depth=0, state=None, idx=(2, 2)) -> None:
        self.state = state if state else START_STATE
        self.parent = parent
        self.action = action
        self.cost = cost
        self.depth = depth
        self.zero_idx = idx

#Функция передвижения нуля
def move(node, direction):
    state = deepcopy(node.state)
    i, j = node.zero_idx[0], node.zero_idx[1]
    match direction:
        case "right":
            if j > 1:
                return None
            j += 1 
            state[i][j - 1] = state[i][j]
        case "left":
            if j < 1:
                return None
            j -= 1
            state[i][j + 1] = state[i][j]
        case "down":
            if i > 1:
                return None
            i += 1
            state[i - 1][j] = state[i][j]
        case "up":
            if i < 1:
                return None
            i -= 1
            state[i + 1][j] = state[i][j]
        case _:
            return None


    state[i][j] = 0
    next_node = Node(
        state=state,
        parent=node,
        action=direction,
        cost=node.cost + 1,
        idx=(i, j)
    )
    return next_node

#Вывод состояния узла
def print_state(node):
    print("---------")
    state = node.state
    for i in range(3):
        print(state[i])
    print("Path-Cost:", node.cost)
    print("Depth:", node.depth)
    print("---------")

#Поиск всех детей узла
def child_nodes(node):
    child_nodes_list = set()
    for direction in ["left", "up", "down", "right"]:
        next_node = move(node, direction)
        if next_node != None:
            child_nodes_list.add(next_node)
    return child_nodes_list

#Проверка достижения целевого состояния
def check_node(node):
    return node.state == TARGET_STATE