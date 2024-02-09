from structures import *

def print_state(state):
    for i in range(3):
        print(state[i])

start = Node(action=None)
next = Action.up(start)
print_state(start.state)
print('--------')
print_state(next.state)