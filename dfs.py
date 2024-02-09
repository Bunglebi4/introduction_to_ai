from structures import *
        
start = Node(action=None)
print_state(start)
print("------------")
for node in child_nodes(start):
    print_state(node)
    print("------------")
