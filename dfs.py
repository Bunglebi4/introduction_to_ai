from structures import *
import sys
sys.setrecursionlimit(1000000)

def dfs(node, manual, visited=set(), frontier=[], depth=0):
    node.depth = depth    
    if check_node(node):
        print("Достигнута целевое состояние!")
        return node
    else:
        depth += 1

    visited.add(hash(tuple(map(tuple, node.state))))
    children = [child for child in child_nodes(node) if hash(tuple(map(tuple, child.state))) not in visited]
    if manual:
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
        for frontier_node in frontier:
            print_state(frontier_node)
   
        input("Нажмите ENTER для следующего шага")
        frontier.extend(children)

    for child in children:
        result = dfs(child, manual, visited, frontier, depth)
        if result is not None:
            return result
    print("penis")
    return None

# Пример использования
initial_node = Node(action=None)
result_node = dfs(initial_node, False)
print_state(result_node)
input("Press Enter")