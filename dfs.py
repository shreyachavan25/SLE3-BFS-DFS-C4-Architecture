import time

# Same graph used for BFS and DFS
graph = {
    'A': ['B', 'C'],
    'B': ['D'],
    'C': ['G'],
    'D': ['E'],
    'E': ['F'],
    'F': [],
    'G': []
}


def dfs(graph, start, goal):
    stack = [start]
    visited = set()
    nodes_expanded = 0

    while stack:
        node = stack.pop()

        if node in visited:
            continue

        visited.add(node)
        nodes_expanded += 1

        if node == goal:
            return nodes_expanded

        for neighbour in reversed(graph[node]):
            if neighbour not in visited:
                stack.append(neighbour)

    return nodes_expanded


# Test cases
test_cases = [
    ("Best Case", 'A', 'A'),
    ("Average Case", 'A', 'C'),
    ("Worst Case", 'A', 'G')
]

# Number of repetitions for average timing
number_of_runs = 10000

print("DFS PERFORMANCE ANALYSIS")
print("------------------------")

for case_name, start, goal in test_cases:

    # Find nodes expanded
    nodes = dfs(graph, start, goal)

    # Measure total time for repeated executions
    start_time = time.perf_counter()

    for _ in range(number_of_runs):
        dfs(graph, start, goal)

    end_time = time.perf_counter()

    total_time = end_time - start_time
    average_time = (total_time / number_of_runs) * 1000

    print("\n", case_name)
    print("Start Node:", start)
    print("Goal Node:", goal)
    print("Nodes Expanded:", nodes)
    print("Average Execution Time (ms):", average_time)


# Repeated workload for py-spy
print("\nRunning DFS workload for py-spy...")

end_time = time.time() + 10

while time.time() < end_time:
    dfs(graph, 'A', 'G')

print("DFS py-spy workload completed.")