from queue import Queue
'''
A graph is a collection of nodes where each node point to another one
'''


class Edge:
    def __init__(self, src, dest):
        self.src = src
        self.dest = dest


# A class to represent a graph object
class Graph:
    # Constructor
    def __init__(self, edges, N):
        # allocate memory for the adjacency list
        self.adj = [[] for _ in range(N)]

        # add edges to the undirected graph
        for current in edges:
            # allocate node in adjacency list from src to dest
            self.adj[current.src].append(current.dest)


# Function to print adjacency list representation of a graph
def printGraph(graph):
    for src in range(len(graph.adj)):
        # print current vertex and all its neighboring vertices
        for dest in graph.adj[src]:
            print(f"({src} —> {dest}) ", end="")
        print()


if __name__ == '__main__':
    # Input: Edges in a directed graph
    edges = [Edge(0, 1), Edge(1, 2), Edge(2, 0), Edge(2, 1),
             Edge(3, 2), Edge(4, 5), Edge(5, 4)]

    # Input: No of vertices
    N = 6

    # construct a graph from a given list of edges
    graph = Graph(edges, N)

    # print adjacency list representation of the graph
    printGraph(graph)

