import heapq

# Define the goal state
goal_state = ((1, 2, 3), (8, 0, 4), (7, 6, 5))

# Define possible moves
moves = [(0, 1), (0, -1), (1, 0), (-1, 0)]

# Helper function to calculate the Manhattan distance
def manhattan_distance(state):
    distance = 0
    for i in range(3):
        for j in range(3):
            if state[i][j] != 0:
                goal_row, goal_col = divmod(state[i][j] - 1, 3)
                distance += abs(i - goal_row) + abs(j - goal_col)
    return distance

# Define a class for puzzle states
class PuzzleState:
    def __init__(self, state, parent=None, move=None):
        self.state = state
        self.parent = parent
        self.move = move
        self.g = 0  # Cost from the initial state
        self.h = manhattan_distance(state)  # Heuristic: Manhattan distance

    def __lt__(self, other):
        return (self.g + self.h) < (other.g + other.h)

# A* algorithm
def astar(initial_state):
    open_set = [PuzzleState(initial_state)]
    closed_set = set()

    while open_set:
        current_state = heapq.heappop(open_set)

        if current_state.state == goal_state:
            # Reconstruct and return the path
            path = []
            while current_state:
                path.append(current_state.state)
                current_state = current_state.parent
            return list(reversed(path))

        closed_set.add(current_state.state)

        for move in moves:
            new_row, new_col = current_state.state.index(0), current_state.state[current_state.state.index(0)].index(0)
            next_row, next_col = new_row + move[0], new_col + move[1]

            if 0 <= next_row < 3 and 0 <= next_col < 3:
                new_state = list(list(row) for row in current_state.state)
                new_state[new_row][new_col], new_state[next_row][next_col] = new_state[next_row][next_col], new_state[new_row][new_col]
                new_state = tuple(tuple(row) for row in new_state)

                if new_state not in closed_set:
                    child_state = PuzzleState(new_state, current_state, move)
                    child_state.g = current_state.g + 1

                    # Check if this state is already in the open set with a better g value
                    found_better = False
                    for open_state in open_set:
                        if open_state.state == new_state and open_state.g <= child_state.g:
                            found_better = True
                            break

                    if not found_better:
                        heapq.heappush(open_set, child_state)

    return None

def main():
    print("Enter the initial state:")
    initial_state = []
    for _ in range(3):
        row = tuple(map(int, input().split()))
        initial_state.append(row)

    solution_path = astar(tuple(initial_state))

    if solution_path:
        print("Solution steps:")
        for step in solution_path:
            for row in step:
                print(row)
            print()
    else:
        print("No solution found.")

if __name__ == "__main__":
    main()

