
from collections import deque

class State:
    def __init__(self, missionaries, cannibals, boat, parent=None):
        self.missionaries = missionaries
        self.cannibals = cannibals
        self.boat = boat
        self.parent = parent

    def __eq__(self, other):
        return (self.missionaries, self.cannibals, self.boat) == (other.missionaries, other.cannibals, other.boat)

    def __hash__(self):
        return hash((self.missionaries, self.cannibals, self.boat))

    def is_valid(self):
        if self.missionaries < 0 or self.cannibals < 0 or self.missionaries > 3 or self.cannibals > 3:
            return False
        if self.missionaries < self.cannibals and self.missionaries > 0:
            return False
        if 3 - self.missionaries < 3 - self.cannibals and 3 - self.missionaries > 0:
            return False
        return True

    def is_final(self):
        return self.missionaries == 0 and self.cannibals == 0 and self.boat == 'right'

def generate_moves():
    return [(1, 0), (2, 0), (1, 1), (0, 1), (0, 2)]

def apply_move(state, move):
    new_state = State(state.missionaries, state.cannibals, state.boat, parent=state)
    
    if state.boat == 'left':
        new_state.missionaries -= move[0]
        new_state.cannibals -= move[1]
        new_state.boat = 'right'
    else:
        new_state.missionaries += move[0]
        new_state.cannibals += move[1]
        new_state.boat = 'left'

    return new_state
 
def solve_game():
    initial_state = State(3, 3, 'left')
    visited_states = set()
    queue = deque([initial_state])

    while queue:
        current_state = queue.popleft()
        if current_state.is_final():
            solution = []
            while current_state:
                solution.insert(0, current_state)
                current_state = current_state.parent
            return solution
        visited_states.add(current_state)

        possible_moves = generate_moves()
        for move in possible_moves:
            new_state = apply_move(current_state, move)
            if new_state.is_valid() and new_state not in visited_states:
                new_state.parent = current_state
                queue.append(new_state)

    return None

solution = solve_game()

def print_state(state):
    left_missionaries = state.missionaries
    right_missionaries = 3 - state.missionaries
    left_cannibals = state.cannibals
    right_cannibals = 3 - state.cannibals
    boat_position = "left" if state.boat == "left" else "right"
    
    print("Left: {}M {}C | Boat: {} | Right: {}M {}C".format(
        left_missionaries, left_cannibals, boat_position, right_missionaries, right_cannibals))

if solution:
    for index, state in enumerate(solution):
        print("Step {}: ".format(index + 1), end="")
        print_state(state)
else:
    print("No solution found.")
