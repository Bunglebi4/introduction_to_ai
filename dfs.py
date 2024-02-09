from structures import *

def dfs(start):
    print_state(start)
    print(check_node(start))

target = Node(action=None, state=TARGET_STATE)
start = Node(action=None)
dfs(start)
dfs(target)