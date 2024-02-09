import collections
from copy import deepcopy
from collections import deque

#Класс узла
class Node:
    def __init__(self, action: str, parent=None, depth=0, state=None, idx=(2, 2)) -> None:
        self.state = state if state else [[6, 2, 8], [4, 1, 7], [5, 3, 0]]
        self.parent = parent
        self.action = action
        self.cost = 0
        self.depth = depth
        self.zero_idx = idx

#Функция передвижения нуля
def move(direction, node):
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
        depth=node.depth + 1,
        idx=(i, j)
    )
    return next_node

#Вывод состояния узла
def print_state(node):
    state = node.state
    for i in range(3):
        print(state[i])

#Поиск всех детей узла
def child_nodes(node):
    child_nodes_list = []
    for direction in ["left", "right", "up", "down"]:
        next_node = move(direction, node)
        if next_node != None:
            child_nodes_list.append(next_node)
    return child_nodes_list
