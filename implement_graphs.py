# G = V + E

def create_adjacency_list(vertices, edge_list):
    """Create an adjacency dictionary from bare nodes and edges."""
    # create an empty dictionary
    adjacency_dict = {}

    # fill it with one key for each node. the value of each node should be an 
    # empty list.
    for vertex in range(vertices):
        adjacency_dict[vertex] = []

    # populate each list with neighbour nodes. 
    # each edge has an origin and a destination in each tuple.
    # go to the origin and append the destination.
    for (origin, destination) in edge_list:
        adjacency_dict[origin].append(destination)
    
    return adjacency_dict

V = 4
E = [(0, 1), (1, 2), (0, 3)]

# adjacency_dict = create_adjacency_list(V, E)
# print(adjacency_dict)
# returns: 
# {0: [1, 3], 1: [2], 2: [], 3: []}

def create_weighted_adjacency_list(vertices, edge_list):
    """Create an adjacency list with weighted edges."""
    # create an empty dictionary
    weighted_adjacency_list = {}

    # create one key for each node
    # each node should have an empty list for a value
    for vertex in range(vertices):
        weighted_adjacency_list[vertex] = []
    

    # populate each list with a new tuple: the neighbour node and the weight.
    for origin, destination, weight in edge_list:
        weighted_adjacency_list[origin].append((destination, weight))  
    
    return weighted_adjacency_list

WV = 4
# origin, destination, weight
WE = [(0, 1, 5), (1, 2, 10), (0, 3, 15)]

# weighted_adjacency_list = create_weighted_adjacency_list(WV, WE)
# print(weighted_adjacency_list)
# returns
# 0 is connected to 1 with a weight of 5. Also connected to 3 with a weight of 15
# {0: [(1, 5), (3, 15)], 1: [(2, 10)], 2: [], 3: []}


def create_weighted_adjacency_list_with_dictionaries(vertices, edge_list):
    """Create an adjacency list with weighted edges, with dicts."""
    # create an empty dictionary
    weighted_adjacency_list = {}

    # create one key for each node
    # each node should have an empty dict for a value
    for vertex in range(vertices):
        weighted_adjacency_list[vertex] = {}
    

    # populate each dict with the neighbour node as key and weight as value.
    for origin, destination, weight in edge_list:
        weighted_adjacency_list[origin][destination] = weight   
    
    return weighted_adjacency_list

# This is a bit nicer for lookups 
weighted_adjacency_dicts = create_weighted_adjacency_list_with_dictionaries(WV, WE)
print(weighted_adjacency_dicts)
# returns 
# {0: {1: 5, 3: 15}, 1: {2: 10}, 2: {}, 3: {}}

# I think usually people use numpy or pandas to create an adjacency matrix.
# It is possible to do it with vanilla Python - here is what is shown on AlgoDaily:

# Graph via adjacency list
graph = {
    "A": ["A", "B", "C"],
    "B": ["A", "C", "D"],
    "C": ["A", "B", "E"],
    "D": ["C", "D"],
    "E": ["B", "E"],
}

keys = sorted(graph.keys())
size = len(keys)

matrix = [[0] * size for i in range(size)]

# We iterate over the key:value entries in the dictionary first,
# then we iterate over the elements within the value
for a, b in [(keys.index(a), keys.index(b)) for a, row in graph.items() for b in row]:
    # Use 1 to represent if there's an edge
    # Use 2 to represent when node meets itself in the matrix (A -> A)
    matrix[a][b] = 2 if (a == b) else 1

print(matrix)

# algos: 
# BFS
# DFS
# Topological Sort
# Djikstra

# have a quick look at the others! make flashcards but don't memorise