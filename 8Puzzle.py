import queue

class State:
    def __init__(self, state, parent, action, depth, cost):
        self.state = state
        self.parent = parent
        self.action = action
        self.depth = depth
        self.cost = cost

def bfs(initial, goal):
    q = queue.Queue()
    q.put(initial)
    while not q.empty():
        current = q.get()
        if current.state == goal:
            return current
        children = expand(current, goal)
        for child in children:
            q.put(child)
    return None

def expand(current, goal):
    x, y = find_blank_square(current.state)
    children = []
    moves = [[-1, 0], [1, 0], [0, -1], [0, 1]]
    for move in moves:
        child_x, child_y = x + move[0], y + move[1]
        if is_valid_move(child_x, child_y, current.state):
            new_state = create_new_state(current.state, x, y, child_x, child_y)
            cost = current.cost + 1
            depth = current.depth + 1
            children.append(State(new_state, current, move, depth, cost))
    return children

def create_new_state(state, x1, y1, x2, y2):
    new_state = [row[:] for row in state]
    temp = new_state[x2][y2]
    new_state[x2][y2] = new_state[x1][y1]
    new_state[x1][y1] = temp
    return new_state

def is_valid_move(x, y, state):
    n = len(state)
    return 0 <= x < n and 0 <= y < n

def find_blank_square(state):
    for i in range(len(state)):
        for j in range(len(state[i])):
            if state[i][j] == 0:
                return i, j

def print_solution(goal):
    moves = []
    current = goal
    while current.parent is not None:
        moves.append(current.action)
        current = current.parent
    moves.reverse()
    print("Moves:", moves)
    print("Number of moves:", len(moves))

def main():
    initial = [[2, 8, 3], [1, 6, 4], [7, 0, 5]]
    goal = [[1, 2, 3], [8, 0, 4], [7, 6, 5]]
    initial = State(initial, None, None, 0, 0)
    goal = bfs(initial, goal)
    if goal is None:
        print("No solution found.")
    else:
        print_solution(goal)

if __name__ == '__main__':
    main()
