"""
Module: simple_graph
License: MIT
Author: Prashant Garg
Date: 2025-08-10

Description:
------------
This module provides an implementation of an undirected graph using an adjacency list.
"""

class Graph:
    """
    A class to represent an undirected graph using an adjacency list.

    Attributes
    ----------
    adjacency_list : dict
        A dictionary to store the adjacency list of the graph.
    """

    def __init__(self):
        """
        Initializes a new instance of the Graph class.
        """
        self.adjacency_list: dict[str, set[str]] = {}

    def add_vertex(self, new_vertex: str) -> bool:
        """
        Adds a vertex to the graph.

        Parameters
        ----------
        new_vertex : str
            The vertex to be added to the graph.

        Returns
        -------
        bool
            True if the vertex was added, False if it already exists.
        """
        if new_vertex in self.adjacency_list:
            return False
        self.adjacency_list[new_vertex] = set()
        return True

    def add_edge(self, vertex_one: str, vertex_two: str) -> bool:
        """
        Adds an undirected edge between two vertices in the graph.

        Parameters
        ----------
        vertex_one : str
            The first vertex of the edge.
        vertex_two : str
            The second vertex of the edge.

        Returns
        -------
        bool
            True if the edge was added, False if one or both vertices do not exist.
        """
        if vertex_one not in self.adjacency_list or vertex_two not in self.adjacency_list:
            return False
        self.adjacency_list[vertex_one].add(vertex_two)
        self.adjacency_list[vertex_two].add(vertex_one)
        return True

    def remove_edge(self, vertex_one: str, vertex_two: str) -> bool:
        """
        Removes an undirected edge between two vertices in the graph.

        Parameters
        ----------
        vertex_one : str
            The first vertex of the edge.
        vertex_two : str
            The second vertex of the edge.

        Returns
        -------
        bool
            True if the edge was removed, False if one or both vertices do not exist.
        """
        if vertex_one not in self.adjacency_list or vertex_two not in self.adjacency_list:
            return False
        self.adjacency_list[vertex_one].discard(vertex_two)
        self.adjacency_list[vertex_two].discard(vertex_one)
        return True

    def remove_vertex(self, vertex_to_remove: str) -> bool:
        """
        Removes a vertex and all its associated edges from the graph.

        Parameters
        ----------
        vertex_to_remove : str
            The vertex to be removed from the graph.

        Returns
        -------
        bool
            True if the vertex was removed, False if it does not exist.
        """
        if vertex_to_remove not in self.adjacency_list:
            return False

        # Get neighbors before removing the vertex
        neighbors = self.adjacency_list[vertex_to_remove].copy()

        # Remove the vertex from the adjacency list
        self.adjacency_list.pop(vertex_to_remove)

        # Remove the vertex only from its actual neighbors
        for neighbor in neighbors:
            self.adjacency_list[neighbor].discard(vertex_to_remove)

        return True

    def print_adjacency_matrix(self):
        """
        Prints the adjacency matrix of the graph.
        """
        existing_vertices = list(self.adjacency_list.keys())
        matrix = [[0] * len(existing_vertices) for _ in range(len(existing_vertices))]

        for i, vertex in enumerate(existing_vertices):
            for neighbor in self.adjacency_list[vertex]:
                matrix[i][existing_vertices.index(neighbor)] = 1

        print("  ", " ".join(existing_vertices))
        for i, row in enumerate(matrix):
            print(existing_vertices[i], " ".join(map(str, row)))


if __name__ == "__main__":
    graph = Graph()
    vertices = ["A", "B", "C", "D", "E", "F"]
    edges = [
        ("A", "B"),
        ("A", "C"),
        ("B", "D"),
        ("C", "D"),
        ("C", "E"),
        ("D", "E"),
        ("E", "F"),
    ]

    for v in vertices:
        graph.add_vertex(v)

    for v_one, v_two in edges:
        graph.add_edge(v_one, v_two)

    graph.print_adjacency_matrix()
