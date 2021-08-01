# Python program for Dijkstra's
# single source shortest
# path algorithm. The program
# is for adjacency matrix
# representation of the graph

from collections import defaultdict


# Class to represent a graph
class Graph:

    forward_table = list()

    # A utility function to find the
    # vertex with minimum dist value, from
    # the set of vertices still in queue
    def minDistance(self, dist, queue):
        # Initialize min value and min_index as -1
        minimum = float("Inf")
        min_index = -1

        # from the dist array,pick one which
        # has min value and is till in queue
        for i in range(len(dist)):
            if dist[i] < minimum and i in queue:
                minimum = dist[i]
                min_index = i
        return min_index

    # Function to print shortest path
    # from source to j
    # using parent array
    def printPath(self, parent, j):
        global res

        # print("DEBUG", parent[j])

        # Base Case : If j is source
        if parent[j] == -1:
            print(j)
            res += str(j)
            return
        self.printPath(parent, parent[j])
        print(j)
        res += str(j)


    # A utility function to print
    # the constructed distance
    # array
    def printSolution(self, dist, parent, src):
        print("Vertex \t\tDistance from Source\tPath")
        for i in range(0, len(dist)):
            if i == src:
                continue
            global res
            res = ""
            print("\n%d --> %d \t\t%d \t\t\t\t\t" % (src, i, dist[i])),
            self.printPath(parent, i)
            print("Next Hop", res[1])
            self.forward_table.append([str(src), str(i), res[1]])


    '''Function that implements Dijkstra's single source shortest path
    algorithm for a graph represented using adjacency matrix
    representation'''

    def dijkstra(self, graph, src):

        self.forward_table = list()

        row = len(graph)
        col = len(graph[0])

        # The output array. dist[i] will hold
        # the shortest distance from src to i
        # Initialize all distances as INFINITE
        dist = [float("Inf")] * row

        # Parent array to store
        # shortest path tree
        parent = [-1] * row

        # Distance of source vertex
        # from itself is always 0
        dist[src] = 0

        # Add all vertices in queue
        queue = []
        for i in range(row):
            queue.append(i)
        # print("DDD", queue)

        # Find shortest path for all vertices
        while queue:

            # Pick the minimum dist vertex
            # from the set of vertices
            # still in queue
            # print("DDD", dist)

            u = self.minDistance(dist, queue)

            # remove min element
            queue.remove(u)

            # Update dist value and parent
            # index of the adjacent vertices of
            # the picked vertex. Consider only
            # those vertices which are still in
            # queue
            for i in range(col):
                '''Update dist[i] only if it is in queue, there is
                an edge from u to i, and total weight of path from
                src to i through u is smaller than current value of
                dist[i]'''
                if graph[u][i] and i in queue:
                    if dist[u] + graph[u][i] < dist[i]:
                        dist[i] = dist[u] + graph[u][i]
                        parent[i] = u

        # print the constructed distance array

        self.printSolution(dist, parent, src)


res = str()
# g = Graph()
#
# graph = [[0, 4, 0, 0, 0, 0, 0, 8, 0],
#          [4, 0, 8, 0, 0, 0, 0, 11, 0],
#          [0, 8, 0, 7, 0, 4, 0, 0, 2],
#          [0, 0, 7, 0, 9, 14, 0, 0, 0],
#          [0, 0, 0, 9, 0, 10, 0, 0, 0],
#          [0, 0, 4, 14, 10, 0, 2, 0, 0],
#          [0, 0, 0, 0, 0, 2, 0, 1, 6],
#          [8, 11, 0, 0, 0, 0, 1, 0, 7],
#          [0, 0, 2, 0, 0, 0, 6, 7, 0]
#          ]

# Print the solution
# g.dijkstra(graph, 0)


# This code is contributed by Neelam Yadav
