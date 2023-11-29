def is_valid(state):
    for side in state:
        husbands = [p for p in side if p[0] == 'H']
        wives = [p for p in side if p[0] == 'W']
        
        if wives and len(husbands) < len(wives):
            return False
    return True

def cross_river(state, move):
    new_state = [list(side) for side in state]
    for person in move:
        for side in new_state:
            if person in side:
                side.remove(person)
                break
    new_side = 1 if state[0] is new_state[0] else 0
    new_state[new_side].append(person)
    return [tuple(side) for side in new_state]

def solve_jealous_husbands(initial_state):
    visited_states = set()
    stack = [(initial_state, [])]
    
    while stack:
        current_state, moves = stack.pop()
        if current_state in visited_states:
            continue
        
        visited_states.add(current_state)
        
        if all(len(side) == 0 for side in current_state[0]):
            return moves
        
        for move in possible_moves:
            new_state = cross_river(current_state, move)
            if is_valid(new_state) and new_state not in visited_states:
                new_moves = moves + [move]
                stack.append((new_state, new_moves))
    
    return None

# The initial state contains the husbands and wives on one side of the river.
initial_state = (
    (('H1', 'H2', 'H3'), ('W1', 'W2', 'W3')),
    ()
)

# Possible moves: 1 or 2 people can cross the river
possible_moves = [
    ['H1'], ['H2'], ['H3'], ['W1'], ['W2'], ['W3'],
    ['H1', 'H2'], ['H1', 'H3'], ['W1', 'W2'], ['W1', 'W3']
]

solution = solve_jealous_husbands(initial_state)

if solution:
    for step, move in enumerate(solution, start=1):
        print(f"Step {step}: {move}")
else:
    print("No solution found.")

