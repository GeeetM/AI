import heapq
from collections import deque

# Define the goal state
goal_state = [[1, 2, 3], [8, 0, 4], [7, 6, 5]]

# Define the heuristic function (Manhattan distance)
def heuristic(state):
    distance = 0
    for i in range(3):
        for j in range(3):
            num = state[i][j]
            if num != 0:
                row = (num - 1) // 3
                col = (num - 1) % 3
                distance += abs(i - row) + abs(j - col)
    return distance

# Define the A* algorithm
def solve_puzzle(start_state):
    # Define the movements: up, down, left, right
    movements = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    queue = []
    heapq.heappush(queue, (0, 0, start_state, None))
    visited = set()
    while queue:
        _, cost, current_state, prev_move = heapq.heappop(queue)
        if current_state == goal_state:
            return construct_path(prev_move)
        visited.add(tuple(map(tuple, current_state)))
        zero_row, zero_col = find_zero(current_state)
        for move_row, move_col in movements:
            new_row = zero_row + move_row
            new_col = zero_col + move_col
            if 0 <= new_row < 3 and 0 <= new_col < 3:
                new_state = [row[:] for row in current_state]
                new_state[zero_row][zero_col] = new_state[new_row][new_col]
                new_state[new_row][new_col] = 0
                if tuple(map(tuple, new_state)) not in visited:
                    priority = cost + 1 + heuristic(new_state)
                    heapq.heappush(queue, (priority, cost + 1, new_state, new_state[zero_row][zero_col]))

# Helper function to find the position of 0 in the puzzle
def find_zero(state):
    for i in range(3):
        for j in range(3):
            if state[i][j] == 0:
                return i, j

# Helper function to construct the path from start to goal state
def construct_path(last_move):
    path = deque()
    while last_move:
        path.appendleft(last_move)
        last_move = last_move[3]
    return path

# Get user input for the initial state
print("Enter the initial state of the puzzle (one row at a time, with spaces in between numbers):")
start_state = []
for _ in range(3):
    row = list(map(int, input().split()))
    start_state.append(row)

# Test the A* algorithm
path = solve_puzzle(start_state)
if path is None:
    print("No solution found!")
else:
    print("Solution found!")
    for move in path:
        print(move)
