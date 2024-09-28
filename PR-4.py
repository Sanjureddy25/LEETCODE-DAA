import heapq
def prims_algorithm(graph, start_vertex):
    mst_edges = []  
    visited = set()  
    min_heap = [(0, start_vertex, None)]  
    while min_heap:
        weight, current_vertex, from_vertex = heapq.heappop(min_heap)
        if current_vertex in visited:
            continue
        visited.add(current_vertex)
        if from_vertex is not None: 
            mst_edges.append((from_vertex, current_vertex, weight))
        for neighbor, edge_weight in graph[current_vertex]:
            if neighbor not in visited:
                heapq.heappush(min_heap, (edge_weight, neighbor, current_vertex))
    return mst_edges

# Example Usage
if __name__ == "__main__":
    graph = {
        'A': [('B', 4), ('C', 3)],
        'B': [('A', 4), ('C', 1), ('D', 2)],
        'C': [('A', 3), ('B', 1), ('D', 4)],
        'D': [('B', 2), ('C', 4)]
    }

    start_vertex = 'A'
    mst = prims_algorithm(graph, start_vertex)

    print("Edges in the Minimum Spanning Tree (MST):")
    for edge in mst:
        print(f"{edge[0]} - {edge[1]} with weight {edge[2]}")
        
OUTPUT:-

Edges in the Minimum Spanning Tree (MST):
A - C with weight 3
C - B with weight 1
B - D with weight 2
