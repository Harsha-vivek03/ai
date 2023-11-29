def tsp_dfs(graph, current_node, visited, num_visited, path_length, min_path, min_path_order):
    if num_visited == len(graph):
        if path_length + graph[current_node][0] < min_path[0]:
            min_path[0] = path_length + graph[current_node][0]
            min_path_order[0] = [i + 1 for i, city_visited in enumerate(visited) if city_visited]
        return
    visited[current_node] = True
    for next_node in range(len(graph)):
        if not visited[next_node]:
            tsp_dfs(graph, next_node, visited, num_visited + 1, path_length + graph[current_node][next_node], min_path, min_path_order)
    visited[current_node] = False
def tsp():
    num_cities = int(input("Enter the number of cities: "))
    graph = []
    print("Enter the distance matrix:")
    for _ in range(num_cities):
        row = list(map(int, input().split()))
        graph.append(row)
    visited = [False] * num_cities
    min_path = [float('inf')]
    min_path_order = [[]]
    tsp_dfs(graph, 0, visited, 1, 0, min_path, min_path_order)
    return min_path[0], min_path_order[0]
min_distance, city_order = tsp()
print("Minimum distance:", min_distance)
print("City order in minimum path:", ", ".join([f"City {city}" for city in city_order]))

