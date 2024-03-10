import sys
import time
from collections import deque
from copy import deepcopy
from typing import List

# Определение начального и целевого состояний
START_STATE = [[7, 2, 4], [5, 0, 6], [8, 3, 1]]
TARGET_STATE = [[1, 2, 3], [4, 5, 6], [7, 8, 0]]


# Класс узла
class Node:
    def __init__(self, state, parent=None, cost=0, depth=0) -> None:
        self.state = state
        self.parent = parent
        self.cost = cost
        self.depth = depth


# Функция для нахождения индекса пустой клетки
def find_empty(state):
    for i in range(3):
        for j in range(3):
            if state[i][j] == 0:
                return i, j


# Функция для перемещения
def move(node, direction):
    state = deepcopy(node.state)
    i, j = find_empty(state)

    if direction == "right" and j < 2:  # Проверяем, что можем сдвинуть вправо
        state[i][j], state[i][j + 1] = state[i][j + 1], state[i][j]  # Меняем местами "ноль" и соседний элемент
    elif direction == "left" and j > 0:  # Проверяем, что можем сдвинуть влево
        state[i][j], state[i][j - 1] = state[i][j - 1], state[i][j]
    elif direction == "down" and i < 2:  # Проверяем, что можем сдвинуть вниз
        state[i][j], state[i + 1][j] = state[i + 1][j], state[i][j]
    elif direction == "up" and i > 0:  # Проверяем, что можем сдвинуть вверх
        state[i][j], state[i - 1][j] = state[i - 1][j], state[i][j]

    return state


# Функция для проверки, достигли ли мы целевого состояния
def is_goal(state):
    return state == TARGET_STATE


# Эвристическая функция h1 - число фишек, стоящих не на своем месте
def h1(state):
    count = 0
    for i in range(3):
        for j in range(3):
            if state[i][j] != TARGET_STATE[i][j]:
                count += 1
    return count


# Эвристическая функция h2 - суммарное по всем фишкам число шагов до целевого положения (манхэттенское расстояние)
def h2(state):
    total_distance = 0
    for i in range(3):
        for j in range(3):
            value = state[i][j]
            if value != 0:
                target_i, target_j = divmod(value - 1, 3)  # Позиция целевой клетки для текущего значения
                total_distance += abs(target_i - i) + abs(target_j - j)
    return total_distance


# Функция для поиска пути с использованием алгоритма A*
def astar(start_state, heuristic_func):
    start_node = Node(start_state)
    frontier = deque([(start_node, 0)])  # Очередь с приоритетом, где приоритет - оценка стоимости пути
    visited = set()
    visited_states = {}  # Таблица замещения для хранения посещенных состояний и их стоимости
    while frontier:
        current_node, current_cost = frontier.popleft()
        current_state = current_node.state
        if is_goal(current_state):
            return current_node
        if tuple(map(tuple, current_state)) not in visited:
            visited.add(tuple(map(tuple, current_state)))
            visited_states[tuple(map(tuple, current_state))] = current_cost
            for direction in ["left", "right", "up", "down"]:
                new_state = move(current_node, direction)
                if new_state:
                    new_node = Node(new_state, current_node, current_cost + 1, current_node.depth + 1)
                    new_state_tuple = tuple(map(tuple, new_state))
                    if new_state_tuple not in visited_states or current_cost + 1 < visited_states[new_state_tuple]:
                        frontier.append((new_node, current_cost + 1 + heuristic_func(new_state)))
                        visited_states[new_state_tuple] = current_cost + 1
                    frontier = deque(sorted(frontier, key=lambda x: x[1]))  # Сортировка очереди по оценке стоимости
    return None


# Функция для вывода пути
def print_path(node):
    path = []
    while node:
        path.append(node.state)
        node = node.parent
    path.reverse()
    for state in path:
        print_state(state)


# Функция для вывода состояния
def print_state(state):
    for row in state:
        print(row)
    print()


# Функция для выполнения алгоритма A* с выводом промежуточных состояний
def run_astar(start_state, heuristic_func):
    print("Starting state:")
    print_state(start_state)
    print("Goal state:")
    print_state(TARGET_STATE)
    print("Using heuristic function:", heuristic_func.__name__)
    start_time = time.time()
    result_node = astar(start_state, heuristic_func)
    end_time = time.time()
    if result_node:
        print("Solution found:")
        print_path(result_node)
        print("Total cost:", result_node.cost)
        print("Total depth:", result_node.depth)
    else:
        print("Solution not found.")
    print("Time taken:", end_time - start_time, "seconds")


# Запуск алгоритма с использованием эвристической функции h1
run_astar(START_STATE, h1)

# Запуск алгоритма с использованием эвристической функции h2
run_astar(START_STATE, h2)