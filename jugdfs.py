class State:
    def __init__(self, jug1, jug2):
        self.jug1 = jug1
        self.jug2 = jug2
    def __eq__(self, other):
        return self.jug1 == other.jug1 and self.jug2 == other.jug2
    def __hash__(self):
        return hash((self.jug1, self.jug2))
def water_jug_dfs(capacity_jug1, capacity_jug2, target):
    visited = set()
    def dfs(state):
        if state.jug1 == target or state.jug2 == target:
            return [state]
        visited.add(state)
        actions = []
        # Fill jug 1
        if state.jug1 < capacity_jug1:
            next_state = State(capacity_jug1, state.jug2)
            if next_state not in visited:
                actions = dfs(next_state)
                if actions:
                    actions.insert(0, state)
                    return actions
        # Fill jug 2
        if state.jug2 < capacity_jug2:
            next_state = State(state.jug1, capacity_jug2)
            if next_state not in visited:
                actions = dfs(next_state)
                if actions:
                    actions.insert(0, state)
                    return actions
        # Empty jug 1
        if state.jug1 > 0:
            next_state = State(0, state.jug2)
            if next_state not in visited:
                actions = dfs(next_state)
                if actions:
                    actions.insert(0, state)
                    return actions
        # Empty jug 2
        if state.jug2 > 0:
            next_state = State(state.jug1, 0)
            if next_state not in visited:
                actions = dfs(next_state)
                if actions:
                    actions.insert(0, state)
                    return actions
        # Pour water from jug 1 to jug 2
        if state.jug1 > 0 and state.jug2 < capacity_jug2:
            pour = min(state.jug1, capacity_jug2 - state.jug2)
            next_state = State(state.jug1 - pour, state.jug2 + pour)
            if next_state not in visited:
                actions = dfs(next_state)
                if actions:
                    actions.insert(0, state)
                    return actions
        # Pour water from jug 2 to jug 1
        if state.jug2 > 0 and state.jug1 < capacity_jug1:
            pour = min(state.jug2, capacity_jug1 - state.jug1)
            next_state = State(state.jug1 + pour, state.jug2 - pour)
            if next_state not in visited:
                actions = dfs(next_state)
                if actions:
                    actions.insert(0, state)
                    return actions
        return []
    initial_state = State(0, 0)
    solution = dfs(initial_state)
    return solution
def print_steps(solution):
    if not solution:
        print("No solution found.")
        return
    for i, state in enumerate(solution):
        print(f"Step {i + 1}: Jug 1: {state.jug1}, Jug 2: {state.jug2}")
if __name__ == "__main__":
    # Prompt the user for inputs
    capacity_jug1 = int(input("Enter the capacity of the first jug: "))
    capacity_jug2 = int(input("Enter the capacity of the second jug: "))
    target_amount = int(input("Enter the target amount to measure: ")) 
    print("Solving the water jug problem using DFS...")
    solution = water_jug_dfs(capacity_jug1, capacity_jug2, target_amount)
    print_steps(solution)
