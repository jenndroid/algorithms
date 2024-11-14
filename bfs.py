# Working!
from collections import deque

def breadth_first_search(adjacency_list, sought, to_check, checked, steps):
    """Implement BFS."""

    if len(to_check) == 0:
        print(f"No more nodes left to check. Sought node '{sought}' not found in graph.")
        return
    
    head = to_check.popleft()
    
    if head not in checked:
        if head == sought:
            print(f"Found sought node '{sought}' in {steps} steps from start node")
            return 
        
        # add head's neighbour nodes to queue, only if we haven't seen it before
        # Add each neighbour indivdually
        # I think we could also have
        # to_check.extend(adjacency_list[head])
        # could only push on neighboursn not in checked:
        # if neighbour not in checked
        for neighbour in adjacency_list[head]:
            to_check.append(neighbour)
        
        # add the head to checked
        checked[head] = True

        # increment nodes checked by 1
        steps += 1
    
    # else if we had checked that node, just carry on
    # with remaining queue
    return breadth_first_search(
        adjacency_list,
        sought,
        to_check,
        checked,
        steps
    )


breadth_first_search(
    adjacency_list = {
    'A': ['B', 'C'], 
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F', 'G'],
    'D': ['B'],
    'E': ['B'],
    'F': ['C'],
    'G': ['C']
},
sought = 'G', # prints Found sought node in 6 steps from start node - correct
# sought = 'Z', # prints No more nodes left to check. Sought node 'Z' not found in graph. - correct
# all other sought options print correct step number!
to_check = deque(['A']),
checked = {},
steps = 0
)
