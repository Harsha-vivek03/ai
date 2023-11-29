from collections import deque
class State:
    def __init__(self, fox, goose, beans, man, parent=None):
        self.fox = fox
        self.goose = goose
        self.beans = beans
        self.man = man
        self.parent = parent
    def __eq__(self, other):
        return (self.fox, self.goose, self.beans, self.man) == (other.fox, other.goose, other.beans, other.man)
    def __hash__(self):
        return hash((self.fox, self.goose, self.beans, self.man))
    def is_valid(self):
        if (self.goose == self.fox and self.man != self.goose) or \
           (self.goose == self.beans and self.man != self.goose):
            return False
        return True
    def is_final(self):
        return self.fox == 'right' and self.goose == 'right' and self.beans == 'right' and self.man == 'right'
    def __repr__(self):
        return f"fox: {self.fox}, goose: {self.goose}, beans: {self.beans}, man: {self.man}"
def generate_moves():
    return ['fox', 'goose', 'beans', 'man']
def apply_move(state, move):
    new_state = State(state.fox, state.goose, state.beans, state.man)
    if move == 'fox':
        new_state.fox = 'right' if state.fox == 'left' else 'left'
        new_state.man = 'right' if state.man == 'left' else 'left'
    elif move == 'goose':
        new_state.goose = 'right' if state.goose == 'left' else 'left'
        new_state.man = 'right' if state.man == 'left' else 'left'
    elif move == 'beans':
        new_state.beans = 'right' if state.beans == 'left' else 'left'
        new_state.man = 'right' if state.man == 'left' else 'left'
    elif move == 'man':
        new_state.man = 'right' if state.man == 'left' else 'left'
    return new_state
def solve_game():
    initial_state = State('left', 'left', 'left', 'left')
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
        for move in generate_moves():
            new_state = apply_move(current_state, move)
            if new_state.is_valid() and new_state not in visited_states:
                new_state.parent = current_state
                queue.append(new_state)
    return None
solution = solve_game()
if solution:
    for index, state in enumerate(solution):
        print("Step {}: fox: {}, goose: {}, beans: {}, man: {}".format(
            index + 1, state.fox, state.goose, state.beans, state.man))
else:
    print("No solution found.")
