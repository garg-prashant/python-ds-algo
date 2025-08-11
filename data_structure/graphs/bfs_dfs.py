"""
This module provides implementations of Breadth-First Search (BFS) and Depth-First Search (DFS)
for traversing graphs. The graph is represented as a dictionary where keys are node identifiers
and values are lists of adjacent nodes.
"""

from collections import deque
from typing import Dict, List, Set, Optional

Graph = Dict[str, List[str]]


def bfs(graph_data: Graph, start: str) -> Set[str]:
    """
    Perform a breadth-first search on a graph starting from a given node.

    Args:
        graph_data (Graph): The graph to traverse.
        start (str): The starting node for the BFS.

    Returns:
        Set[str]: A set of nodes visited during the BFS.
    """
    visited: Set[str] = {start}
    queue: deque[str] = deque([start])

    while queue:
        v = queue.popleft()
        for n in graph_data.get(v, []):
            if n not in visited:
                visited.add(n)
                queue.append(n)
    return visited


def dfs(graph_data: Graph, vertex: str, visited: Optional[Set[str]] = None) -> Set[str]:
    """
    Perform a depth-first search on a graph starting from a given node.

    Args:
        graph_data (Graph): The graph to traverse.
        vertex (str): The starting node for the DFS.
        visited (Optional[Set[str]]): A set of nodes already visited. Defaults to None.

    Returns:
        Set[str]: A set of nodes visited during the DFS.
    """
    if visited is None:
        visited = set()
    if vertex in visited:
        return visited

    visited.add(vertex)
    for n in graph_data.get(vertex, []):
        if n not in visited:
            dfs(graph_data, n, visited)
    return visited


if __name__ == "__main__":
    graph_example: Graph = {
        "A": ["B", "C"],
        "B": ["A", "D", "E"],
        "C": ["A", "F"],
        "D": ["B"],
        "E": ["B", "F"],
        "F": ["C", "E"],
    }

    print(bfs(graph_example, "A"))  # {'A', 'B', 'C', 'D', 'E', 'F'}
    print(dfs(graph_example, "A"))  # {'A', 'B', 'D', 'E', 'C', 'F'} (order can vary)
