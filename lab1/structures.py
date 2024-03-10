import collections
from copy import deepcopy
from collections import deque

START_STATE = [[6, 2, 8], [4, 1, 7], [5, 3, 0]]
TARGET_STATE = [[0, 1, 2], [3, 4, 5], [6, 7, 8]]


# Класс узла
class Node:
    def __init__(self, action: str, parent=None, cost=0, depth=0, state=None, idx=(2, 2)) -> None:
        self.state = state if state else START_STATE
        self.parent = parent
        self.action = action
        self.cost = cost
        self.depth = depth
        self.zero_idx = idx


# Функция передвижения нуля
def move(node, direction, bfs=False):
    state = deepcopy(node.state)
    i, j = node.zero_idx[0], node.zero_idx[1]

    if direction == "right" and j < 2:  # Проверяем, что можем сдвинуть вправо
        state[i][j], state[i][j + 1] = state[i][j + 1], state[i][j]  # Меняем местами "ноль" и соседний элемент
        j += 1  # Обновляем индекс столбца
    elif direction == "left" and j > 0:  # Проверяем, что можем сдвинуть влево
        state[i][j], state[i][j - 1] = state[i][j - 1], state[i][j]
        j -= 1
    elif direction == "down" and i < 2:  # Проверяем, что можем сдвинуть вниз
        state[i][j], state[i + 1][j] = state[i + 1][j], state[i][j]
        i += 1  # Обновляем индекс строки
    elif direction == "up" and i > 0:  # Проверяем, что можем сдвинуть вверх
        state[i][j], state[i - 1][j] = state[i - 1][j], state[i][j]
        i -= 1
    else:
        return None

    next_node = Node(
        state=state,
        parent=node,
        action=direction,
        cost=node.cost + 1,
        idx=(i, j)
    )
    return next_node



# Вывод состояния узла
def print_state(node):
    print("---------")
    state = node.state
    for i in range(3):
        print(state[i])
    print("Path-Cost:", node.cost)
    print("---------")


# Поиск всех детей узла
def child_nodes(node):
    child_nodes_list = set()
    for direction in ["left", "right", "up", "down"]:
        next_node = move(node, direction)
        if next_node is not None:
            child_nodes_list.add(next_node)
    return child_nodes_list


# Проверка достижения целевого состояния
def check_node(node):
    return node.state == TARGET_STATE
