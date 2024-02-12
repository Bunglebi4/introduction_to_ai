"""
function BFS(v : Node) : Boolean;
begin
  enqueue(v);

  while queue is not empty do
  begin
    curr := dequeue();

    if is_goal(curr) then
    begin
      BFS := true;
      exit;
    end;

    mark(curr);

    for next in successors(curr) do
      if not marked(next) then
      begin
        enqueue(next);
      end;
  end;

  BFS := false;
end;
"""
from collections import deque

from structures import TARGET_STATE, check_node, child_nodes, print_state, Node


def ucs(v, depth=0, cost=0, manual=False, frontier=[], visited=set()):
    # if check_node(v) == TARGET_STATE:
    #     print("target state: \n")
    #     return v
    # cost += 1
    # visited.add(hash(tuple(map(tuple, v.state))))
    # next_neighbours = [child for child in child_nodes(v) if hash(tuple(map(tuple, child.state))) not in visited]
    # if manual:
    #     print("Текущая вершина, выбираемая для раскрытия на данном шаге:")
    #     print_state(v)
    #
    #     print("Добавленные вершины после раскрытия:")
    #     for child in next_neighbours:
    #         print_state(child)
    #
    #     all_children = [child for child in child_nodes(v)]
    #     print("Выявленные повторные вершины:")
    #     for child in all_children:
    #         if hash(tuple(map(tuple, child.state))) in visited:
    #             print_state(child)
    #
    #     print("Вершины, ждущие раскрытия:")
    #     for frontier_node in frontier:
    #         print_state(frontier_node)
    #
    #     input("Нажмите ENTER для следующего шага")
    #     frontier.extend(next_neighbours)
    queue = deque()
    queue.append(v)
    i = 0
    while True:
        current = queue.popleft()
        visited.add(hash(tuple(map(tuple, current.state))))
        if current.state == TARGET_STATE:
            print_state(current)
            break
        next_neighbours = [child for child in child_nodes(current) if
                           hash(tuple(map(tuple, child.state))) not in visited]
        for child in next_neighbours:
            queue.append(child)
        i += 1


initial_node = Node(action=None)
ucs(initial_node, False)
input("Press Enter")
