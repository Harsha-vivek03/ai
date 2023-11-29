from collections import deque
class State:
    def __init__(self, jug1, jug2, path):
        self.jug1 = jug1
        self.jug2 = jug2
        self.path = path
    def __eq__(self, other):
        return self.jug1 == other.jug1 and self.jug2 == other.jug2
    def __hash__(self):
        return hash((self.jug1, self.jug2))
    def __str__(self):
        return f'({self.jug1}, {self.jug2})'
def is_valid(jug1, jug2, max_jug1, max_jug2):
    return 0 <= jug1 <= max_jug1 and 0 <= jug2 <= max_jug2
def bfs_water_jug(max_jug1, max_jug2, target):
    visited = set()
    start_state = State(0, 0, [])
    queue = deque([start_state])
    visited.add(start_state)
    while queue:
        current_state = queue.popleft()
        if current_state.jug1 == target or current_state.jug2 == target:
            return current_state
        # Fill jug1
        if is_valid(max_jug1, current_state.jug2, max_jug1, max_jug2):
            new_state = State(max_jug1, current_state.jug2, current_state.path + [(max_jug1, current_state.jug2)])
            if new_state not in visited:
                queue.append(new_state)
                visited.add(new_state)
        # Fill jug2
        if is_valid(current_state.jug1, max_jug2, max_jug1, max_jug2):
            new_state = State(current_state.jug1, max_jug2, current_state.path + [(current_state.jug1, max_jug2)])
            if new_state not in visited:
                queue.append(new_state)
                visited.add(new_state)
        # Pour from jug1 to jug2
        if is_valid(current_state.jug1 - min(current_state.jug1, max_jug2 - current_state.jug2),
                    current_state.jug2 + min(current_state.jug1, max_jug2 - current_state.jug2),
                    max_jug1, max_jug2):
            new_state = State(current_state.jug1 - min(current_state.jug1, max_jug2 - current_state.jug2),
                              current_state.jug2 + min(current_state.jug1, max_jug2 - current_state.jug2),
                              current_state.path + [(current_state.jug1 - min(current_state.jug1, max_jug2 - current_state.jug2),
                                                    current_state.jug2 + min(current_state.jug1, max_jug2 - current_state.jug2))])
            if new_state not in visited:
                queue.append(new_state)
                visited.add(new_state)
        # Pour from jug2 to jug1
        if is_valid(current_state.jug1 + min(current_state.jug2, max_jug1 - current_state.jug1),
                    current_state.jug2 - min(current_state.jug2, max_jug1 - current_state.jug1),
                    max_jug1, max_jug2):
            new_state = State(current_state.jug1 + min(current_state.jug2, max_jug1 - current_state.jug1),
                              current_state.jug2 - min(current_state.jug2, max_jug1 - current_state.jug1),
                              current_state.path + [(current_state.jug1 + min(current_state.jug2, max_jug1 - current_state.jug1),
                                                    current_state.jug2 - min(current_state.jug2, max_jug1 - current_state.jug1))])
            if new_state not in visited:
                queue.append(new_state)
                visited.add(new_state)
    return None
# Example usage
max_jug1 = int(input("Enter the maximum capacity of jug 1: "))
max_jug2 = int(input("Enter the maximum capacity of jug 2: "))
target = int(input("Enter the target amount of water to measure: "))
result_state = bfs_water_jug(max_jug1, max_jug2, target)
if result_state:
    print("Water jug configuration to measure", target, "liters:")
    for step in result_state.path:
        print("Step:", step)
else:
    print("Target amount of water cannot be measured with the given jug capacities.")
