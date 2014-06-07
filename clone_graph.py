# Definition for a undirected graph node
# class UndirectedGraphNode:
#     def __init__(self, x):
#         self.label = x
#         self.neighbors = []

class Solution:
    # @param node, a undirected graph node
    # @return a undirected graph node
    def cloneGraph(self, node):
        if node == None:
            return None
        root = UndirectedGraphNode(node.label)
        root.neighbors = node.neighbors
        stack = [node]
        visited = {node:root}
        while len(stack) > 0:
            last = stack.pop()
            cp_last = visited[last]
            for neigh in last.neighbors:
                if not neigh in visited:
                    cp_neigh = UndirectedGraphNode(neigh.label)
                    cp_neigh.neighbors = neigh.neighbors
                    visited[neigh] = cp_neigh
                    stack.append(neigh)
        for node in visited:
            cp_node = visited[node]
            cp_node.neighbors = [visited[neigh] for neigh in cp_node.neighbors]
        return root
