"""
Advanced Algorithms HW2: Implement a 2-approximation algorithm for
the metric TSP problem! The code is directly drawn from a very
outstanding existing implementation:
https://github.com/shiThomas/MST-TSP
Hence, the answers are available at the GitHub link above.
Please don't look at it unless you are absolutely stuck!
"""

import math
from tsp_approx_tests import *

##############################################################################


def prim(adjList, adjMat):
    """
    Builds an MST from the given map using the Prim's algorithm, no
    need to change anything.

    Args:
        adjList (list of vertex objects): the list of all neighbors of
            all cities in the map.
        adjMat (list of lists of ints): the 2D array representing the
            distance between two cities.

    Returns:
        nothing (just changes attributes of vertices).
    """
    # initialize all vertexes in the graph
    for vertex in adjList:
        vertex.cost = math.inf
        vertex.prev = None
        vertex.visited = False
        # set the vertex with rank 0 as start
        if vertex.rank == 0:
            start = vertex
            start.cost = 0

    # initialize the priority queue
    Q = MinQueue(adjList)
    while not Q.isEmpty():
        # get the next unvisited vertex and visit it
        v = Q.deleteMin()
        v.visited = True

        # For each edge out of v
        for neigh in v.neigh:

            # If the edge leads out, update
            if not neigh.visited:
                if neigh.cost > adjMat[v.rank][neigh.rank]:
                    neigh.cost = adjMat[v.rank][neigh.rank]
                    neigh.prev = v
    return


##############################################################################


def tsp(adjList, start):
    """
    Uses a 2-approximation to get an approximate solution of the TSP
    problem.

    Args:
        adjList (list of vertex objects): the list of all neighbors of
            all cities in the map.
        start (str): the city where we start our tour.
        (see Map class for more information!)

    Returns:
        tour (list of ints): a tour which is a cycle of cities. Its
            cost is at most twice the optimal solution. It should be an
            array of cities visited in the tour, in the order visited.
            The cities should be denoted by their rank (their numbering
            in adjList).
    """
    # TODO: Your implementation goes here
    tour = None  # replace this with your own implementation
    return tour


##############################################################################


class Vertex:
    """
    Creates and handles a vertex object. Provided for your convenience!
    Don't change anything.

    Attributes:
        rank (int): the rank of this node.
        neigh (list of vertex objects): list of neighbors IN THE
            ORIGINAL GRAPH.
        mstN (list of vertex objects): list of neighbors IN THE MST.
        visited (bool): a flag for whether the vertex has been visited.
        cost (float): the cost of the edge out of the tree.
        prev (vertex object): the previous vertex in the path.
        city (str): the name of the associated city.
    """

    def __init__(self, rank):
        """
        __init__ function to initialize the vertex.

        Args:
            rank (int): rank of the vertex.
        """
        self.rank = rank  # Set the rank of this vertex.
        self.neigh = []  # Set the input neighbors.
        self.mstN = []  # Set the mst neighbors.
        self.visited = False  # Not yet visited.
        self.cost = math.inf  # Infinite cost initially.
        self.prev = None  # No previous node on path yet.
        self.city = ''  # No city initially.
        return

    def __repr__(self):
        """
        Prints only the vertex's city.
        """
        return '%s' % self.city

    def isEqual(self, vertex):
        """
        Compares this vertex to an input vertex object.
        Note: only needs to compare the rank!

        Args:
            vertex (vertex object): vertex created by initializing this
                class.

        Returns:
            (bool): True if ranks are equal, False if unequal.
        """
        return self.rank == vertex.rank

    def __lt__(self, other):
        """
        Overloaded comparison operators for priority queue. Sorted
        by cost.

        Args:
            other (vertex object): another vertex object to compare.

        Returns:
            (bool): True if cost of vertex is less than cost of other,
                else False.
        """
        return self.cost < other.cost


##############################################################################


class Edge:
    """
    Creates and handles edge objects that joins two vertices.
    Provided for your convenience! Don't change anything.

    Attributes:
        vertices (list of strs): list of vertices for this edge.
        weight (int): the weight of this edge.
    """

    def __init__(self, vertex1=None, vertex2=None, weight=math.inf):
        """
        Initializes the edge.

        Args:
            vertex1 (vertex object): first vertex for the edge.
            vertex2 (vertex object): second vertex for the edge.
            weight (int): the weight of the edge.
        """

        self.vertices = [vertex1] + [vertex2]
        self.weight = weight
        return

    def __repr__(self):
        """
        Prints an edge.
        """
        return '(%s,%s): %f' % (
            self.vertices[0].city,
            self.vertices[1].city,
            self.weight,
        )

    """
    Overloaded comparison operators for sorting by weight.
    """

    def __lt__(self, other):
        return self.weight < other.weight

    def __le__(self, other):
        return self.weight <= other.weight

    def __eq__(self, other):
        return self.weight == other.weight

    def __ne__(self, other):
        return self.weight != other.weight

    def __gt__(self, other):
        return self.weight > other.weight

    def __ge__(self, other):
        return self.weight >= other.weight


##############################################################################


class MinQueue:
    """
    Creates and handles a minqueue. Provided for your convenience!
    Don't change anything.

    Attributes:
        array (list of ints): array storing the values in the queue.
    """

    def __init__(self, array=[]):
        """
        Initializes the edge.

        args:
            array (list of ints): the input array to be inserted into
                the queue.
        """
        self.array = array.copy()
        return

    def __repr__(self):
        """
        Prints the array.
        """
        return repr(self.array)

    def isEmpty(self):
        """
        Check if the queue is empty.

        Returns:
            (bool): True if empty, false if not empty.
        """
        if len(self.array) == 0:
            return True
        else:
            return False

    def insert(self, val):
        """
        Inserts an object into the queue.

        Args:
            val (int): value to be inserted into the array.
        """
        self.array.append(val)

    def deleteMin(self):
        """
        Returns the min element and removes it from the queue.
        """
        # Check if empty.
        if len(self.array) == 0:
            raise Exception('Cannot delete min from an empty queue.')

        # Start by considering the first element.
        minVal = self.array[0]
        minInd = 0

        # Loop to find the min element.
        for ind in range(1, len(self.array)):
            if self.array[ind] < minVal:
                minVal = self.array[ind]
                minInd = ind

        # Remove the min and return it.
        self.array.pop(minInd)
        return minVal


##############################################################################


class Map:
    """
    Creates and handles map object.
    TODO: complete the getTSPApprox() and getTSPOptimal() methods.
    Everything else is complete and provided for your convenience.

    Attributes:
        adjMat (list of lists of ints): adjacency matrix storing edge
            weights.
        cities (list of strs): list of city names.
        adjList (list of vertex objects): list of vertices.
        edgeList (list of edge objects): list of edges.
        start (str): starting vertex of the tour.
        mst (list of edge objects): edges in the MST.
        tour (list of vertex ranks): approximate TSP tour.
        tourOpt (list of vertex ranks): optimal TSP tour.
        optTour (str): string displaying the optimal tour.
    """

    def __init__(self, mapNum=0):
        """
        Initializes the map.

        Args:
            mapNum (int): number of the map to use.
        """
        # Get the adjMat, cities, and optTour using mapNum.
        self.adjMat, self.cities, self.optTour = getMap(mapNum)[0:3]
        self.mapNum = mapNum

        # Create the adjList of vertices
        self.adjList = []
        for rank in range(0, len(self.cities)):
            v = Vertex(rank)
            self.adjList.append(v)

        # Create the list of edges and fill the vertex.neigh values.
        # Fill in the cities while we are at it.
        self.edgeList = []
        for r1 in range(0, len(self.adjMat)):
            v1 = self.adjList[r1]
            v1.city = self.cities[r1]
            for r2 in range(r1 + 1, len(self.adjMat[r1])):
                if self.adjMat[r1][r2] != 0:
                    v2 = self.adjList[r2]
                    v1.neigh.append(v2)
                    v2.neigh.append(v1)
                    e = Edge(v1, v2, self.adjMat[r1][r2])
                    self.edgeList.append(e)

        # Sort the edges.
        self.edgeList.sort()

        # Set start to the 0 ranked vertex (the first city).
        self.start = self.adjList[0]

        # Empty MST initially.
        self.mst = []

        # Empty tour initially.
        self.tour = []
        self.tourOpt = []
        return

    def __repr__(self):
        """
        Prints a map.
        """
        # First the MST edges.
        s = ''
        s += '\nMST Edges:\n'
        w = 0
        for e in self.mst:
            s += repr(e) + '\n'
            w += e.weight
        s += '\nMST Weight:\n%f\n' % w

        # Now the tour.
        s += '\nTSP Approx. Tour:\n'
        w = 0
        if len(self.tour) > 0:
            for r in range(0, len(self.tour) - 1):
                s += self.cities[self.tour[r]] + '\n'
                w += self.adjMat[self.tour[r]][self.tour[r + 1]]
            s += self.cities[self.tour[0]] + '\n'
        else:
            w = math.inf
        s += '\nTSP Approx. Tour Weight:\n%f\n' % w

        # Now the optimal tour.
        s += self.optTour

        # Return the repr string.
        return s

    def printList(self):
        """
        Cleanly prints the adjaceny list. Note: skips vertices with
        no neighbors.
        """
        for vertex in self.adjList:
            if len(vertex.neigh) > 0:
                print('Rank: %d' % vertex.rank)
                print('Neighbors:')
                print(vertex.neigh)
                print('')
        return

    def printMat(self):
        """
        Cleanly prints the adjaceny matrix. Note: for the larger
        matrices, this will still likely be hard to read.
        """
        for row in self.adjMat:
            print(row)
        return

    def printEdges(self):
        """
        Prints the edge list of the map.
        """
        s = 'Edge List:\n'
        for e in self.edgeList:
            s += repr(e) + '\n'
        print(s)
        return

    def getMST(self):
        """
        Uses MSTalg to get the MST and fill in the edges.
        """
        # Call Prim's on the adjList and adjMat.
        # This should update all of the vertices' prev values.
        prim(self.adjList, self.adjMat)
        # Now that we've set all of the prev values, go through each vertex
        # and update its mstN list.
        for v in self.adjList:
            if not v.prev is None:
                v.mstN.append(v.prev)
                v.prev.mstN.append(v)

        # Loop through the vertices and add the MST edges.
        for rank in range(0, len(self.adjList)):
            v = self.adjList[rank]
            for neighbor in v.mstN:
                if neighbor.rank > rank:
                    e = Edge(v, neighbor, self.adjMat[rank][neighbor.rank])
                    self.mst.append(e)
        return

    def getTSPApprox(self):
        """
        Uses the MST to find the approximate solution to TSP.

        Returns:
            nothing (just updates self.tour).

        Raises:
            Exception: if no MST is set.
        """
        if len(self.mst) > 0:
            print()  # replace with your implementation
            # TODO:
            # Complete the TSP Approximation method here
            # Update the Map object with the TSP Approximate tour
        else:
            raise Exception('No MST set!')
        return

    def getTSPOptimal(self):
        """
        Brute-force approach to finding the optimal tour.

        Returns:
            nothing (just updates self.tourOpt).
        """
        # TODO:
        # complete a brute-force TSP solution and replace the
        # following two lines with an actual implementation
        self.tourOpt = getMap(self.mapNum)[3]
        return

    def clearMap(self):
        """
        Resets the MST and tour for the map along with all vertex info.
        """
        # Create the adjList of vertices
        self.adjList = []
        for rank in range(0, len(self.cities)):
            v = Vertex(rank)
            self.adjList.append(v)

        # Create the list of edges and fill the vertex.neigh values.
        # Fill in the cities while we are at it.
        self.edgeList = []
        for r1 in range(0, len(self.adjMat)):
            v1 = self.adjList[r1]
            v1.city = self.cities[r1]
            for r2 in range(r1 + 1, len(self.adjMat[r1])):
                if self.adjMat[r1][r2] != 0:
                    v2 = self.adjList[r2]
                    v1.neigh.append(v2)
                    v2.neigh.append(v1)
                    e = Edge(v1, v2, self.adjMat[r1][r2])
                    self.edgeList.append(e)

        # Sort the edges.
        self.edgeList.sort()

        # Set start to the 0 ranked vertex (the first city).
        self.start = self.adjList[0]

        # Empty MST initially.
        self.mst = []

        # Empty tour initially.
        self.tour = []


##############################################################################

if __name__ == "__main__":
    """
    Here, we run the tests! You want to pass 9/9 MST & TSP tests
    (which will happen if your implementation is correct). You also
    want to pass 4/4 2-approximation tests.
    """

    # Build MST with Prim's Algorithm, then find the approximate
    # solution to the TSP problem. Print the results.
    s = testMSTApprox()
    print(s)

    # Check if the MST approximation approach is a 2-approximation of
    # the optimal solution. In interest of time, only test on the first
    # four maps.
    s = test2approx()
    print(s)
