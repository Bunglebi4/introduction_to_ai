import time

from structures import *
import sys

sys.setrecursionlimit(100000)
import sys
import sys

def dfs(node, manual, visited=set(), frontier=[], depth=0, iterations=0, total_nodes=0):
    node.depth = depth
    iterations += 1  # Увеличиваем счетчик итераций на 1 при каждом вызове функции
    total_nodes += 1  # Увеличиваем счетчик общего количества узлов на 1 при каждом вызове функции
    if check_node(node):
        return node, iterations, total_nodes, visited, frontier  # Возвращаем также множество посещенных состояний и приоритетную очередь
    else:
        depth += 1
    visited.add(hash(tuple(map(tuple, node.state))))
    children = [child for child in child_nodes(node) if hash(tuple(map(tuple, child.state))) not in visited]
    if manual:
        frontier_size_before = len(frontier)
        frontier.extend(children)
        print("Текущая вершина, выбираемая для раскрытия на данном шаге:")
        print_state(node)

        print("Добавленные вершины после раскрытия:")
        for child in children:
            print_state(child)

        all_children = [child for child in child_nodes(node)]
        print("Выявленные повторные вершины:")
        for child in all_children:
            if hash(tuple(map(tuple, child.state))) in visited:
                print_state(child)

        print("Вершины, ждущие раскрытия:")
        for frontier_node in frontier[frontier_size_before:]:
            print_state(frontier_node)

        input("Нажмите ENTER для следующего шага")

    for child in children:
        result, iterations, total_nodes, visited, frontier = dfs(child, manual, visited, frontier, depth, iterations, total_nodes)  # Обновляем значения итераций, общего количества узлов, множества посещенных состояний и приоритетной очереди
        if result is not None:
            return result, iterations, total_nodes, visited, frontier

    return None, iterations, total_nodes, visited, frontier  # Возвращаем None вместо только None, чтобы передать количество итераций, общее количество узлов, множество посещенных состояний и приоритетную очередь


# Пример использования
initial_node = Node(action=None)
start_time = time.time()
result_node, iterations, total_nodes, visited, frontier = dfs(initial_node, False)
end_time = time.time()

print("Достигнуто целевое состояние!")
print("Количество пройденных узлов:", len(visited))
print("Итерации:", iterations)
print("Затраты памяти:", sys.getsizeof(visited) + sys.getsizeof(frontier), "bytes")
print("Общее количество узлов:", total_nodes)
print("Время:", end_time-start_time)
print_state(result_node)
input("Press Enter")
