import collections
from collections import deque

class Node:
    def __init__(self, action: str, parent = None, depth=0, state=None, idx=(2, 2)) -> None:
        self.state = state if state else [[6, 2, 8], [4, 1, 7], [5, 3, 0]]
        self.parent = parent
        self.action = action
        self.cost = 0
        self.depth = depth
        self.zero_idx = idx


class Action:
    @staticmethod
    def right(state, node):
        i, j = node.zero_idx[0], node.zero_idx[1]
        if j > 1:
            return None
        j += 1
        state[i][j - 1] = state[i][j]
        state[i][j] = 0
        next_node = Node(
            state=state,
            parent=node,
            action="right",
            depth=node.depth + 1,
            idx=(i, j)
        )
        return next_node

    @staticmethod
    def left(state, node):
        i, j = node.zero_idx[0], node.zero_idx[1]
        if j < 1:
            return None
        j -= 1
        state[i][j + 1] = state[i][j]
        state[i][j] = 0
        next_node = Node(
            state=state,
            parent=node,
            action="left",
            depth=node.depth + 1,
            idx=(i, j)
        )
        return next_node

    @staticmethod
    def down(state, node):
        i, j = node.zero_idx[0], node.zero_idx[1]
        if i > 1:
            return None
        i += 1
        state[i - 1][j] = state[i][j]
        state[i][j] = 0
        next_node = Node(
            state=state,
            parent=node,
            action="down",
            depth=node.depth + 1,
            idx=(i, j)
        )
        return next_node

    @staticmethod
    def up(state, node):
        i, j = node.zero_idx[0], node.zero_idx[1]
        if i < 1:
            return None
        i -= 1
        state[i + 1][j] = state[i][j]
        state[i][j] = 0
        next_node = Node(
            state=state,
            parent=node,
            action="up",
            depth=node.depth + 1,
            idx=(i, j)
        )
        return next_node
