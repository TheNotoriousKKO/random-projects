import random
import heapq
import matplotlib.pyplot as plt
import networkx as nx


def generate_graph(num_nodes, max_weight=10, connectivity=0.3):
    """
    Generates a weighted graph with nodes and edges.
    :param num_nodes: Number of nodes in the graph.
    :param max_weight: Maximum weight of edges.
    :param connectivity: Probability of creating an edge between nodes.
    :return: A graph represented as an adjacency list.
    """
    graph = {i: [] for i in range(num_nodes)}
    for i in range(num_nodes):
        for j in range(i + 1, num_nodes):
            if random.random() < connectivity:
                weight = random.randint(1, max_weight)
                graph[i].append((j, weight))
                graph[j].append((i, weight))
    return graph


def visualize_graph(graph, title="Graph Visualization"):
    """
    Visualizes the entire graph.
    :param graph: The graph to visualize (adjacency list).
    :param title: Title of the visualization.
    """
    G = nx.Graph()
    for node, edges in graph.items():
        for edge, weight in edges:
            G.add_edge(node, edge, weight=weight)
    pos = nx.spring_layout(G)
    edge_labels = nx.get_edge_attributes(G, "weight")
    nx.draw(G, pos, with_labels=True, node_color="lightgray", node_size=600, font_size=8)
    nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels)
    plt.title(title)
    plt.show()


def visualize_path(graph, path, start, end):
    """
    Visualizes the graph with the path highlighted.
    :param graph: The graph to visualize (adjacency list).
    :param path: The path to highlight.
    :param start: Start node.
    :param end: End node.
    """
    G = nx.Graph()
    for node, edges in graph.items():
        for edge, weight in edges:
            G.add_edge(node, edge, weight=weight)

    subgraph_nodes = set(path)
    for node in path:
        subgraph_nodes.update(neighbor for neighbor, _ in graph[node])
    subgraph = G.subgraph(subgraph_nodes)

    pos = nx.circular_layout(subgraph)
    edge_labels = nx.get_edge_attributes(subgraph, "weight")

    nx.draw(subgraph, pos, with_labels=True, node_color="lightgray", node_size=600, font_size=8)
    nx.draw_networkx_edge_labels(subgraph, pos, edge_labels=edge_labels)

    if path:
        path_edges = [(path[i], path[i + 1]) for i in range(len(path) - 1)]
        nx.draw_networkx_nodes(subgraph, pos, nodelist=path, node_color="skyblue", node_size=700)
        nx.draw_networkx_edges(subgraph, pos, edgelist=path_edges, edge_color="red", width=2)

    plt.legend(
        handles=[
            plt.Line2D([0], [0], color="skyblue", marker="o", linestyle="", markersize=10, label=f"Start ({start})"),
            plt.Line2D([0], [0], color="red", marker="o", linestyle="", markersize=10, label=f"End ({end})"),
        ],
        loc="upper left",
        frameon=True,
        title="Legend",
    )
    plt.title("Simplified Graph Visualization with Path Highlighted")
    plt.show()


def dijkstra(graph, start, end):
    """
    Finds the shortest path using Dijkstra's algorithm.
    :param graph: The graph (adjacency list).
    :param start: Start node.
    :param end: End node.
    :return: Shortest path and total cost.
    """
    pq = [(0, start)]
    distances = {node: float('inf') for node in graph}
    distances[start] = 0
    previous = {node: None for node in graph}

    while pq:
        current_distance, current_node = heapq.heappop(pq)

        if current_node == end:
            break

        for neighbor, weight in graph[current_node]:
            distance = current_distance + weight
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                previous[neighbor] = current_node
                heapq.heappush(pq, (distance, neighbor))

    path = []
    current = end
    while current is not None:
        path.append(current)
        current = previous[current]
    path.reverse()

    return path, distances[end] if distances[end] != float('inf') else None


def dfs(graph, start, end, path=None, visited=None):
    """
    Finds a path using Depth-First Search.
    :param graph: The graph (adjacency list).
    :param start: Start node.
    :param end: End node.
    :param path: Current path (used in recursion).
    :param visited: Visited nodes (used in recursion).
    :return: A path if found, otherwise None.
    """
    if path is None:
        path = []
    if visited is None:
        visited = set()

    path.append(start)
    visited.add(start)

    if start == end:
        return path

    for neighbor, _ in graph[start]:
        if neighbor not in visited:
            result = dfs(graph, neighbor, end, path, visited)
            if result:
                return result

    path.pop()
    return None


if __name__ == "__main__":
    num_nodes = int(input("Enter the number of nodes: "))
    graph = generate_graph(num_nodes, max_weight=15, connectivity=0.5)

    print("Graph (Adjacency List):")
    for node, edges in graph.items():
        print(f"{node}: {edges}")

    visualize_graph(graph, title="Graph Before Pathfinding")

    start_node = int(input("Enter the start node: "))
    end_node = int(input("Enter the end node: "))

    print("\nFinding shortest path using Dijkstra's algorithm...")
    path, cost = dijkstra(graph, start_node, end_node)
    if path and cost is not None:
        print(f"Path: {path}, Total cost: {cost}")
    else:
        print("No path found.")
        path = []

    visualize_path(graph, path, start_node, end_node)
