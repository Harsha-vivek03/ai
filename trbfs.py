from collections import deque
def tsp_bfs(graph):
    num_cities = len(graph)
    starting_node = 0
    min_distance = float('inf')
    min_path_order = []
    queue = deque([(starting_node, [starting_node])])
    while queue:
        current_node, path_order = queue.popleft()
        if len(path_order) == num_cities:
            path_order.append(starting_node)
            total_distance = calculate_path_length(graph, path_order)
            if total_distance < min_distance:
                min_distance = total_distance
                min_path_order = path_order
        else:
            for next_node in range(num_cities):
                if next_node not in path_order:
                    new_path_order = path_order[:]
                    new_path_order.append(next_node)
                    queue.append((next_node, new_path_order))
    return min_distance, min_path_order
def calculate_path_length(graph, path_order):
    total_distance = 0
    for i in range(len(path_order) - 1):
        from_city = path_order[i]
        to_city = path_order[i + 1]
        total_distance += graph[from_city][to_city]
    return total_distance
def main():
    num_cities = int(input("Enter the number of cities: "))
    graph = []
    print("Enter the distance matrix:")
    for _ in range(num_cities):
        row = list(map(int, input().split()))
        graph.append(row)
    min_distance, city_order = tsp_bfs(graph)
    print("Minimum distance:", min_distance)
    print("City order in minimum path:", ", ".join([f"City {city+1}" for city in city_order]))
if __name__ == "__main__":
    main()

