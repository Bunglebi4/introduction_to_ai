from queue import PriorityQueue


def get_blank_pos(state):
    for i in range(3):
        for j in range(3):
            if state[i][j] == 0:
                return i, j


def move_blank(state, direction):
    new_state = [row.copy() for row in state]
    x, y = get_blank_pos(state)

    if direction == "up":
        new_state[x][y], new_state[x - 1][y] = new_state[x - 1][y], new_state[x][y]
    elif direction == "down":
        new_state[x][y], new_state[x + 1][y] = new_state[x + 1][y], new_state[x][y]
    elif direction == "left":
        new_state[x][y], new_state[x][y - 1] = new_state[x][y - 1], new_state[x][y]
    elif direction == "right":
        new_state[x][y], new_state[x][y + 1] = new_state[x][y + 1], new_state[x][y]

    return new_state


def manhattan_distance(state):
    goal_state = [[1, 2, 3], [4, 5, 6], [7, 8, 0]]
    distance = 0

    for i in range(3):
        for j in range(3):
            if state[i][j] != 0:
                x, y = divmod(state[i][j] - 1, 3)
                distance += abs(x - i) + abs(y - j)

    return distance


def solve_puzzle(start_state):
    priority_queue = PriorityQueue()
    visited = set()

    priority_queue.put((0, start_state, []))

    while not priority_queue.empty():
        cost, current_state, path = priority_queue.get()

        if current_state == [[1, 2, 3], [4, 5, 6], [7, 8, 0]]:
            return path

        visited.add(tuple(map(tuple, current_state)))

        for direction in ["up", "down", "left", "right"]:
            new_state = move_blank(current_state, direction)
            if tuple(map(tuple, new_state)) not in visited:
                new_path = path.copy()
                new_path.append(direction)
                priority_queue.put((cost + 1 + manhattan_distance(new_state), new_state, new_path))

    return None


start_state = [[2, 3, 6], [1, 5, 8], [4, 7, 0]]
solution = solve_puzzle(start_state)

if solution:
    print(f"Solution: {solution}")
else:
    print("No solution found.")
