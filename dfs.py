from structures import *

start = Node(action=None)
print_state(start)
next = move(start, "up")
next = move(next, "left")
print_state(next)
for node in child_nodes(next):
    print_state(node)