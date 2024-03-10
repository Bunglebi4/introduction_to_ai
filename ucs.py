import sys
from collections import deque
import time

from structures import TARGET_STATE, check_node, child_nodes, print_state, Node


def ucs(v, visited=set()):
    queue = deque()
    queue.append((v, 0))  # Добавляем начальный узел с глубиной 0
    depth = 0
    cost = 0
    i = 0
    start_time = time.time()
    while True:

        current, current_depth = queue.popleft()  # Извлекаем текущий узел и его глубину из очереди
        visited.add(hash(tuple(map(tuple, current.state))))
        if current.state == TARGET_STATE:
            end_time = time.time()
            return current, i, visited, queue, depth, cost, end_time-start_time
        next_neighbours = [(child, current_depth + 1, child.cost) for child in child_nodes(current) if
                           hash(tuple(map(tuple, child.state))) not in visited]
        for child, d, c in next_neighbours:
            queue.append((child, d))  # Добавляем следующего соседа в очередь с его глубиной
            cost += c  # Суммируем стоимость пути
        i += 1
        depth = max(depth, current_depth)  # Обновляем максимальную глубину


initial_node = Node(action=None)

result_node, iterations, visited, queue, max_depth, total_cost, time = ucs(initial_node)
print_state(result_node)
print("Happy Happy Happy")
print("Количество пройденных узлов:", len(visited))
print("Итерации:", iterations)
print("Максимальная глубина:", max_depth)
print("Затраты памяти:", sys.getsizeof(visited) + sys.getsizeof(queue), "bytes")
print("Время:", time, "мс")
print("Общее количество узлов:", iterations + len(visited))
