# Haven't checked yet. Have only used a stack instead of queue to modify
from collections import deque

def depth_first_search(adjacency_list, sought, to_check, checked, steps):
    """Implement DFS."""

    if len(to_check) == 0:
        print(f"No more nodes left to check. Sought node '{sought}' not found in graph.")
        return
    
    head = to_check.pop()
    
    if head not in checked:
        if head == sought:
            print(f"Found sought node '{sought}' in {steps} steps from start node")
            return 
        
        # add head's neighbour nodes to queue, only if we haven't seen it before
        # Add each neighbour indivdually
        # this means that we add C then B to stack for node A, so traverse the left leg first
        for neighbour in range(len(adjacency_list[head]) - 1, -1, -1):
                to_check.append(adjacency_list[head][neighbour])
        
        # add the head to checked
        checked[head] = True

        # increment nodes checked by 1
        steps += 1
    
    # else if we had checked that node, just carry on
    # with remaining queue
    return depth_first_search(
        adjacency_list=adjacency_list,
        sought=sought,
        to_check=to_check,
        checked=checked,
        steps=steps
    )

depth_first_search(
    adjacency_list = {
    'A': ['B', 'C'], 
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F', 'G'],
    'D': ['B'],
    'E': ['B'],
    'F': ['C'],
    'G': ['C']
},
# sought = 'G', # prints Found sought node in 2 steps from start node - correct
# sought = 'Z', No more nodes left to check. Sought node 'Z' not found in graph.
# B gets 1
# C gets 4
# D gets 2
# E gets 3
# F gets 5
# G gets 6
sought = 'G',
to_check = deque(['A']),
checked = {},
steps = 0
)

# when I was pushing neighbour nodes onto the stack in the order they were
# written in the adjacency list, with
# for neighbour in adjacency_list[head]:
#     to_check.append(neighbour)

# interestingly, B gets: Found sought node 'B' in 4 steps from start node - 
# this is because it picks leg C to go down first!
# Because of the stack data structure, for A, the stack looks like:
# adjacency_list{'A' : ['B', 'C']}, so:

# B, C

# I'd have to do some jiggery pokery if I wanted B traversed before A:
# go from the end of the neighbour list to the start and append them in reverse order
# remember range starts from given number, goes to one BEFORE the stop, and you add the step
# so this goes from 1, to 0, with a step down of 1 each time
# for neighbour in range(len(adjacency_list[head]) - 1, -1, -1):
#     to_check.append(adjacency_list[head][neighbour])
# add 1th, then add 0th. So to_check gets
# to_check = ('C', 'B')
# and B gets traversed next


# As the code was,
# traversing the rightmost leg first:
# C gets there in 1 
# D gets there in 6
# E gets there in 5
# F gets there in 3 
# G gets there in 2

# Now, reversing the order in which neighbours are added to the stack
# gets the correct output- traversing left leg first in each case.
