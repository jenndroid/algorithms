def topsort(sorted, indegree_map):
    """Implement Kahn's topological sort."""

    # check length of indegree map is not 0.
    # If so, return - graph must be sorted
    if len(indegree_map.keys()) == 0:
        return sorted
    
    # get a node on which nothing depends
    # get the first entry from indegree where value is 0
    # if none, there's a cycle - tell user and return
    chosen = None
    for node, indegree in indegree_map.items():
        if indegree == 0:
            chosen = node
    
    if chosen == None:
        print("Cycle detected: no nodes have an indegree of 0.")
        print("Topological sort not possible on this graph.")
        return []

    # add this node to sorted
    sorted.append(chosen)

    # remove it from the graph: 
    # remove edges - decrement any it has neighbours by 1 in indegree map
    # remove node itself from indegree map
    if len(adjacency_list[chosen]) != 0:
        for neighbour in adjacency_list[chosen]:
            indegree_map[neighbour] -= 1
    
    indegree_map.pop(chosen)

    return topsort(sorted, indegree_map)


# declare adjacency list
# adjacency_list = {
#     'A': ['B', 'C'],
#     'B': ['C'],
#     'C': []
# }
# calling topsort with following:
# adjacency_list:  {'A': ['B', 'C'], 'B': ['C'], 'C': []}
# indegree_map:  {'A': 0, 'B': 1, 'C': 2}
# gets correct order: ['A', 'B', 'C']

# adjacency_list = {
#     'A': ['B', 'C'],
#     'B': ['C', 'E'],
#     'C': ['D', 'E'],
#     'D': [],
#     'E': ['D']
# }
# calling topsort with following:
# adjacency_list:  {'A': ['B', 'C'], 'B': ['C', 'E'], 'C': ['D', 'E'], 'D': [], 'E': ['D']}
# indegree_map:  {'A': 0, 'B': 1, 'C': 2, 'D': 2, 'E': 2}
# gets correct order: ['A', 'B', 'C', 'E', 'D']

# adjacency_list = {
#     'A': []
# }
# calling topsort with following:
# adjacency_list:  {'A': []}
# indegree_map:  {'A': 0}
# gets correct order: ['A']

adjacency_list = {
    'A': ['B'],
    'B': ['C'],
    'C': ['A']
}
# calling topsort with following:
# adjacency_list:  {'A': ['B'], 'B': ['C'], 'C': ['A']}
# indegree_map:  {'A': 1, 'B': 1, 'C': 1}
# Cycle detected: no nodes have an indegree of 0.
# Topological sort not possible on this graph.
# []

# create indegree map from this list
# key: node name, value: how many incoming edges it has
# set all nodes to 0 first
# indegree_map = {}
# for node in adjacency_list:
#     indegree_map[node] = 0
indegree_map = {k: 0 for k in adjacency_list}
for node in adjacency_list:
    for neighbour in adjacency_list[node]:
        indegree_map[neighbour] += 1

print('calling topsort with following:')
print('adjacency_list: ', adjacency_list)
print('indegree_map: ', indegree_map)

result = topsort(sorted=[], indegree_map=indegree_map)
print(result)